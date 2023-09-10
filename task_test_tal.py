#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

###########################################################

class TurtleTryTal():  
    def __init__(self):
        self.publisher = self.publisher(Twist,'cmd_vel', 10)  
        rospy.init_node('turtle_try_tal_node') 
        while not rospy.is_shutdown():
         rate = rospy.Rate(10) # 10hz
         rate.sleep()

def key_in():
    key = input("w, s, d, a, q <<")

    if key == 'q': 
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z =  0 

    elif key == 'w':
            cmd_vel.linear.x  =  0.5
            cmd_vel.angular.z =  0 


    elif key == 's':
            cmd_vel.linear.x  = -0.5
            cmd_vel.angular.z =  0 
            
    elif key == 'a':
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z =  1.0
            
    elif key == 'd' : 
            cmd_vel.linear.x  =  0
            cmd_vel.angular.z = -1.0
        
    else :
            print("Enter W A S D q key") 
            
       
    mydic = {"q":" q (停止)", "w":" w (前)", "s":" s (後)", "a":" a (左)", "d":" d (右)"}
    val = mydic[key]
    print("入力:"+ val)
      

                             # rospyモジュールの初期化    
if __name__ == '__main__':   #①初期化宣言  最初に実行
     cmd_vel = Twist()
