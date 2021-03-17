#!/usr/bin/env python

import rospy
import random
from utiles import Mapa
from pacman.msg import actions
from pacman.msg import performance
from pacman.srv import mapService
def callback_performance(msg):
    print(msg.lives,"  ",msg.score, "  ",msg.gtime, "  ",msg.performEval )

def control_pacman():
    rospy.init_node('control_pacman', anonymous=True)
    pub = rospy.Publisher('pacmanActions0', actions, queue_size=10)
    rospy.Subscriber('performanceEval', performance, callback_performance)
    try:
        mapRequestClient = rospy.ServiceProxy('pacman_world', mapService)
        resp = mapRequestClient("Eyberth")
        mapa = Mapa(resp)
        print(mapa.obs[0].x, mapa.obs[0].y)
        
        
        rate = rospy.Rate(10) # 10hz
        msg = actions();
        while not rospy.is_shutdown():
            msg.action = random.choice([0,1,2,3,4]);
            pub.publish(msg.action)
            rate.sleep()
        
    except rospy.ServiceException as e:
        print ("Service call failed")
    
    
if __name__ == '__main__':
    try:
        control_pacman()
    except rospy.ROSInterruptException:
        pass
