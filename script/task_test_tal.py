#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

##########################################
#pose使うようにする

class TurtleLTestTal():  
    def __init__(self):
        self.publisher = self.publisher(Twist,'cmd_vel', self.talker_callback, 10)  
             #この辺違うかも　参照：https://wiki-ros-org.translate.goog/turtlesim/Tutorials/Go%20to%20Goal?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=sc
        rospy.init_node('turtle_test_tal_node') 
                        
        print("Enter W A S D Q key")
        print("q:停止 \n   W:↑ \n      A:← D:→  \n   S:↓")


    def talker_callback(self): #引数として渡される関数 callback関数
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
        
############################################


#↑ここまで

    
if __name__ == '__main__':   #①初期化宣言  最初に実行
     turtle_test_tal = TurtleLTestTal()  #ノードの作成
     cmd_vel = Twist()
     rate = rospy.Rate(10) # 10hz
     while not rospy.is_shutdown():
        rospy.publish('cmd_vel') #トピックの名前がcmd_vel
        rate.sleep()
