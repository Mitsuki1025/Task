#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

##################################################

class TurtleTryLis():
    def __init__(self): 
            self.subscription = self.create_subscription(Twist,'cmd_vel', 10) 
            rospy.init_node('turtle_try_tal_node')

    
def main(args=None):
    rospy.init(args=args) # rospyモジュールの初期化
    
if __name__ == '__main__':  # 初期化宣言  最初に実行
    cmd_vel = Twist() 
    rospy.init_node("task_test_lis_node") 
    rospy.spin() 