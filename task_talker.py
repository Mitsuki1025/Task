#!/usr/bin/env python3    

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
    
class TurtleLTalker():  
    def teleop():
        super().__init__('turtle_talker_node') 
        pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=1)
        vel = Twist()
        print("Enter W A S D Q key")
        print("Q:停止 \n   W:↑ \n      A:← D:→  \n   S:↓")
    
     
    def talker_callback(self): #引数として渡される関数 callback関数
        key = input("w:forward, s:backward, d:right, a:left, q:stop <<")
        
        if key == 'q': 
            self.vel.linear.x  =  0
            self.vel.angular.z =  0 

        elif key == 'w':
            self.vel.linear.x  =  0.5

        elif key == 's':
            self.vel.linear.x  = -0.5
            
        elif key == 'a':
            self.vel.angular.z =  1.0
            
        elif key == 'd' : 
            self.vel.angular.z = -1.0
        
        else :
            print("Enter W A S D Q key") 
            
       
        mydic = {"q":" q (停止)", "w":" w (前)", "s":" s (後)", "a":" a (左)", "d":" d (右)"}
        val = mydic[key]
        print("入力:"+ val)
            
        self.publisher.publish(self.vel) #?
        
        
if __name__ == '__main__':  # 初期化宣言 
     rospy.init_node("turtle_talker_node")                   
     rate = rospy.Rate(10)  #１秒に10回?
     rospy.spin()           #ノードが動いている間コールバック関数を呼び続ける
     turtle_talker = TurtleLTalker()  #ノードの作成

     while not rospy.is_shutdown():
           rate.sleep()
    
