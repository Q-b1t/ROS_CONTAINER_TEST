#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import math

PI = math.pi




def turtleCircle(moveMessage,pub):
    moveMessage.linear.x = 1.0
    moveMessage.angular.z = 1.0 
    pub.publish(moveMessage) 
    rate.sleep()





def turtleMove(moveMessage,pub):
    sideLength = 3
    speed = 3
    moveMessage.linear.x = speed

    t0 = rospy.Time.now().to_sec()
    dist = 0

    while dist < sideLength:
        pub.publish(moveMessage)
        t1 = rospy.Time.now().to_sec()
        dist = speed*(t1-t0)

    moveMessage.linear.x = 0
    pub.publish(moveMessage)



def turtleRotate(moveMessage,pub):
	angular_speed = PI*2/4
	moveMessage.angular.z = angular_speed
	t0	= rospy.Time.now().to_sec()
	angle_travelled = 0

	while ( angle_travelled < PI/2.0 ):
		pub.publish(moveMessage)
		t1 = rospy.Time.now().to_sec()
		angle_travelled = angular_speed*(t1-t0)

	moveMessage.angular.z = 0
	pub.publish(moveMessage)	  



def turtleSquare(moveMessage,pub):
    rotations = 0
    square = 4
    while rotations < square:
        turtleRotate(moveMessage,pub)
        #rate.sleep()
        turtleMove(moveMessage,pub)
        #rate.sleep()
        rotations += 1



if __name__ == "__main__":
    publisher = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=1) # topico
    rospy.init_node("tutle_move") # nodo
    rate = rospy.Rate(50) # frequencia
    moveMsg = Twist()
    while not rospy.is_shutdown():
        #turtleCircle(moveMsg,publisher)
        turtleSquare(moveMsg,publisher)
