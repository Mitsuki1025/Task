#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import datetime



###########################################################

class Talker():  
    def __init__(self):
        self.twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    def publish(self):
            cmd_vel = Twist() 
            
            dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得 
            print(f'hour: {dt.hour}, minute: {dt.minute}, second: {dt.second}')  
           
      
            if  (int(dt.hour) <=  11 ): #１時〜１１時
                  cmd_vel.linear.z = -0.3
            elif ( int(dt.hour) ==  12 ): #12時 
                  cmd_vel.linear.y = -0.3
            elif (int(dt.hour) >=  23 ): #１３時から２３時まで
                  cmd_vel.linear.z = 0.3
            else:                   
                  cmd_vel.linear.y = 0.3 #24時 

            self.twist_pub.publish(cmd_vel)
            
                             # rospyモジュールの初期化    
if __name__ == '__main__':   #①初期化宣言  最初に実行
     rospy.init_node("task_test_tal_node", anonymous=True) 
     rate = rospy.Rate(10) # 10hz
     talker = Talker()

     while not rospy.is_shutdown():
         talker.publish()
         rate.sleep()
         

