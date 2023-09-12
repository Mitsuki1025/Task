#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


###########################################################

class TurtleTestTal():  
    def __init__(self):
        self.twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        
    def publish(self):
    
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z =  0 

            cmd_vel.linear.x  =  0.5
            cmd_vel.angular.z =  0 


            cmd_vel.linear.x  = -0.5
            cmd_vel.angular.z =  0 
            
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z =  1.0
            
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z = -1.0
        
            self.twist_pub.publish(cmd_vel)
      

                             # rospyモジュールの初期化    
if __name__ == '__main__':   #①初期化宣言  最初に実行
     cmd_vel = Twist()
     rospy.init_node("task_test_tal_node", anonymous=True) 
     rate = rospy.Rate(10) # 10hz
     
     while not rospy.is_shutdown():
         rate.sleep()
         

