#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import string
import math
import time
import sys


from path_plan_control.srv import nav_one_point 
from aubo_arm_usr.srv import graspcube
from aubo_arm_usr.srv import graspcup
from aubo_arm_usr.srv import armshakehand
from aubo_arm_usr.srv import armmovemotion
from aubo_arm_usr.srv import armshakehead 
from geometry_msgs.msg import PoseStamped 
from std_msgs.msg import String

def move_to_end(x):
    rospy.wait_for_service('/nav_dest') 
    try: 
        nav_point = rospy.ServiceProxy('/nav_dest', nav_one_point) 
        resp1 = nav_point(x[0], x[1], x[2], x[3], x[4])
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e
        
def shake_hand(num):
    rospy.wait_for_service('/shake_hand') 
    try: 
        hand = rospy.ServiceProxy('/shake_hand', armshakehand) 
        resp1 = hand(num)
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e 

def shake_head(num):
    rospy.wait_for_service('/shake_head') 
    try: 
        head = rospy.ServiceProxy('/shake_head', armshakehead) 
        resp1 = head(num)
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e 


def grasp_cube(num):
    rospy.wait_for_service('/graspcube') 
    try: 
        cube = rospy.ServiceProxy('/graspcube', graspcube) 
        resp1 = cube(num)
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e 

def  grasp_cup(num):
    rospy.wait_for_service('/grasp_cup') 
    try: 
        cup = rospy.ServiceProxy('/grasp_cup', graspcup) 
        resp1 = cup(num)
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e 


def move_motion():
    rospy.wait_for_service('/arm_move_motion') 
    try: 
        move_mode = rospy.ServiceProxy('/arm_move_motion', armmovemotion) 
        resp1 = move_mode(0)
        return resp1.is_ok
    except rospy.ServiceException, e: 
        print "Service call failed: %s"%e 
 
def voice(str_word):
    pub = rospy.Publisher("/voiceWords", String, queue_size=1)
    rate = rospy.Rate(1)
    # str_word = "ok" 
    rate.sleep()
    rospy.loginfo(str_word)
    pub.publish(str_word)
    rate.sleep()
    # rospy.loginfo(str_word)
    # pub.publish(str_word)
    # rate.sleep()
    # rospy.loginfo(str_word)
    # pub.publish(str_word)
    # rate.sleep()
        
    # pub.publish(str_word) 


if __name__ == "__main__":
    try:
        rospy.init_node('move_grasp_robot', anonymous=True)
        x = [-0.080742, -0.150223, -0.015729, 0.3, 0.1]
        
        voice("我准备出发了")
        move_to_end(x)
        voice("您好，请问有什么需要")
        
        if(grasp_cube(1)):
            print("grasp a cube end!")
        
        voice("握个手") 
        shake_hand(4)
        voice("再见")
        shake_head(4)
        grasp_cup(1)
        move_motion() 
    except KeyboardInterrupt:
        print("shutting down")



