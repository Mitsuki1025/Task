#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

##################################################

class TurtleListener():
    def __init__(self): #コンストラクタ　__init__
                        #selfはインスタンス変数？
            super().__init__('turtle_listener_node')
            self.subscription = self.create_subscription(Twist,'cmd_vel', self.listener_callback, 10) 
#この辺違うかも　参照：https://wiki-ros-org.translate.goog/turtlesim/Tutorials/Go%20to%20Goal?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=sc
            #subscriberの生成
            #1番目の引数　Twist＝メッセージ型
            #2番目の引数　cmd_vel トピック名　？
            #3番目の引数  callback関数
            #4番目の引数  キューのサイズ　？
            
    # コールバック定義は，受信したデータとともに，情報メッセージをコンソールに出力するだけ．        
    def listener_callback(self, Twist):
            #2番目の引数　Twist＝メッセージ型
            self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z)) 

    
def main(args=None):
    rospy.init(args=args) # rospyモジュールの初期化
    
    
if __name__ == '__main__':  # 初期化宣言  最初に実行
     rospy.init_node("task_test_lis_node") 
     turtle_listener = TurtleListener()   #ノードの作成
     rospy.spin() 
     cmd_vel = Twist()
                          #ノードの破壊したほうがいい？　参照：https://qiita.com/ItoMasaki/items/6acabc94b040f8b0f7cd
