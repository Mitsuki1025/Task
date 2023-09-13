#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import datetime
import time


###########################################################

class Talker():  
    def __init__(self):
        self.twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    def publish(self):
            cmd_vel = Twist() 
            
            t_delta = datetime.timedelta(hours=9)
            JST = datetime.timezone(t_delta, 'JST')
            now = datetime.datetime.now(JST)  
            d = f'{now:%S}'
            
            if  now.second != 0 and now.second != 30:
                time.sleep(1)
                
                if   d == "00" or d == "01" or d == "02" or d == "03" or d == "04" :
                        cmd_vel.linear.y = 0.3   
                elif d == "05" or d == "06" or d == "07" or d == "08" or d == "09" :
                        cmd_vel.linear.x = 0.3
                        cmd_vel.angular.z = 0.3          
                elif   d == "10" or d == "11" :
                         cmd_vel.angular.x = -0.3          

                elif   d == "12" or d == "13" or d == "14":
                        cmd_vel.linear.y = 0.6   
                       
                #八角1
                elif d == "15" or d == "17" or d == "19" or d == "21" or d == "23" or \
                     d == "25" or d == "27" or d == "29" or\
                     d == "47" or d == "49" or d == "51" or d == "53" or d == "55" or \
                     d == "57" or d == "59":
                        cmd_vel.linear.x = 0.49
                        cmd_vel.angular.z = 0.49
                        
                #八角2
                elif d == "16" or d == "18" or d == "20" or d == "22" or d == "24" or \
                     d == "26" or d == "30" or \
                     d == "46" or d == "48" or d == "50" or d == "52" or d == "54" or \
                     d == "56" or d == "58" :            
                        cmd_vel.linear.y = 0.49
                        cmd_vel.angular.z = 0.49        
                
                elif d == "31" or d == "32" or d == "33" or d == "34" or d == "35" :
                        cmd_vel.linear.x =  0.5  

                elif d == "36" or d == "37" or d == "38" or d == "39" or d == "40":
                        cmd_vel.linear.y = - 0.3 
                        cmd_vel.angular.z = 0.3         
         
                else:
                        cmd_vel.linear.x = -0.3
                        cmd_vel.angular.z = -0.3



            self.twist_pub.publish(cmd_vel)
            
                             # rospyモジュールの初期化    
if __name__ == '__main__':   #①初期化宣言  最初に実行
     rospy.init_node("task_test_tal_node", anonymous=True) 
     rate = rospy.Rate(10) # 10hz
     talker = Talker()

     while not rospy.is_shutdown():
         talker.publish()
         rate.sleep()
         

