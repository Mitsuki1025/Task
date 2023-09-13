#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose

##################################################

class Listener():
    def __init__(self): 
        self.twist_sub = rospy.Subscriber('pose',Pose, self.listener_callback ,10) 
        
    def listener_callback(self, Twist):
         rospy.loginfo("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.linear.y,Twist.angular.z)) 

    
if __name__ == '__main__':  # 初期化宣言  最初に実行
    rospy.init_node("task_test_lis_node", anonymous=True) 
    listener = Listener()
    pose = Pose()
    rospy.spin() 
    