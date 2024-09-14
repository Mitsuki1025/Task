import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import mediapipe as mp
from gesture_detection.config import *
from gesture_detection.Logger import Logger
from gesture_detection.Command import Command


class CustomNode(Node):

    def __init__(self):
        super().__init__(NodeName)
        self.cmd_pub = self.create_publisher(String, PublisherName, 10)
        self.img_sub = self.create_subscription(Image, SubscriberName, self.subscribe_img, 10)
        self.timer   = self.create_timer(PublishInterval, self.publish_cmd)
        self.bridge  = CvBridge()

        # Initialize MediaPipe Pose
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
                    min_detection_confidence = MinDetectionConf, 
                    min_tracking_confidence  = MinTrackingConf
                    )

        # Initialize variables
        self.img = None
        self.cmd = Command.STOP

        Logger.info(f'{NodeName} initialized')


    def publish_cmd(self):
        """
        publish current command every second
        """
        msg = String()
        msg.data = self.cmd
        self.cmd_pub.publish(msg)

        if Verbose: Logger.success(f'({ PublisherName }) Published: { msg.data }')


    def subscribe_img(self, data):
        """
        receive image frames via CvBridge
        """
        try:
            self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.process_frame()
        except CvBridgeError as e:
            Logger.fail(f'{e}')


    def extract_bodyparts(self, pose_landmarks) -> dict:
        """
        Example:
        nose_x = bodyparts['NOSE'].x
        """
        bodyparts = { landmark.name: pose_landmarks.landmark[index] for index,landmark in enumerate(self.mp_pose.PoseLandmark) }
        return bodyparts


    def go_left(self, left_wrist, left_shoulder) -> bool:
        """
        extend your left arm to the left
        """
        result: bool =  (left_shoulder.x < left_wrist.x) and (abs(left_shoulder.x - left_wrist.x) > MinNormalWidth)
        if result: self.cmd = Command.GO_LEFT
        return result


    def go_right(self, right_wrist, right_shoulder) -> bool:
        """
        extend your right arm to the right
        """
        result: bool = (right_shoulder.x > right_wrist.x) and (abs(right_shoulder.x - right_wrist.x) > MinNormalWidth)
        if result: self.cmd = Command.GO_RIGHT
        return result

    def turn_left(left_knee, left_heel) -> bool:
        """
        extend your left heel to the left
        """
        return (left_knee.x < left_heel.x)

    def turn_right(right_knee, right_heel) -> bool:
        """
        extend your right heel to the right
        """
        return (right_knee.x > right_heel.x)

    def go_forward(self, right_elbow, right_index) -> bool:
        """
        stretch out your right arm forward
        """
        result = (abs(right_elbow.x - right_index.x) < MaxNormalWidth) and (abs(right_elbow.y - right_index.y) < MaxNormalHeight)
        if result: self.cmd = Command.GO_FORWARD
        return result

    # def stop(left_elbow, left_index, right_elbow, right_index):
    #       return go_forward(left_elbow, left_index) and go_forward(right_elbow, right_index)


    def stop(self, left_hip, left_wrist, left_eye, right_hip, right_wrist, right_eye) -> bool:
        """
        make a X with your arms in front of your chest
        """
        result = (left_hip.y > left_wrist.y > left_eye.y) and (right_hip.y > right_wrist.y > right_eye.y) and (right_wrist.x > left_wrist.x) and (abs(left_wrist.y - right_wrist.y) < MaxNormalHeight)
        if result: self.cmd = Command.STOP
        return result


    def process_frame(self) -> None:
        """
        main process
        """
        try:
            if self.img is None:
                Logger.fail('No frame obtained')
                return

            pose_landmarks = self.pose.process(self.img).pose_landmarks
            mp.solutions.drawing_utils.draw_landmarks(
                self.img, 
                pose_landmarks, 
                self.mp_pose.POSE_CONNECTIONS
            )
            cv2.imshow(f'Mediapipe - { NodeName }', self.img)

            if pose_landmarks == None:
                if Verbose: Logger.warning('No landmark detected')
                return

            if Verbose: Logger.success('Landmarks obtained successfully')

            bodyparts = self.extract_bodyparts(pose_landmarks)

            # Gesture detection
            # if stop(bodyparts['LEFT_ELBOW'], bodyparts['LEFT_INDEX'], bodyparts['RIGHT_ELBOW'], bodyparts['RIGHT_INDEX']):
            if self.stop(bodyparts['LEFT_HIP'], bodyparts['LEFT_WRIST'], bodyparts['LEFT_EYE'], bodyparts['RIGHT_HIP'], bodyparts['RIGHT_WRIST'], bodyparts['RIGHT_EYE']): pass            
            elif self.go_left(bodyparts['LEFT_WRIST'], bodyparts['LEFT_SHOULDER']): pass
            elif self.go_right(bodyparts['RIGHT_WRIST'], bodyparts['RIGHT_SHOULDER']): pass
            elif turn_left(bodyparts['LEFT_KNEE'], bodyparts['LEFT_HEEL']): pass
                if Verbose: print('[+] TURN LEFT')
            elif turn_right(bodyparts['RIGHT_KNEE'], bodyparts['RIGHT_HEEL']): pass
                if Verbose: print('[+] TURN RIGHT')
            elif self.go_forward(bodyparts['RIGHT_ELBOW'], bodyparts['RIGHT_INDEX']): pass
            else: self.cmd = Command.STOP

            if Verbose: Logger.info(f'cmd set to { self.cmd }')

            cv2.waitKey(BufferTime)
        
        except Exception as e:
            Logger.fail(f'{e}')


def main(args=None):
    try:
        rclpy.init(args=args)

        node = CustomNode()
        rclpy.spin(node)

        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

        Logger.info(f'{ NodeName } successfully destroyed')

    except KeyboardInterrupt:
        Logger.warning('Shutting down')
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

