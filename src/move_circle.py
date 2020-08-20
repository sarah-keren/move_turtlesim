#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_circle():
	
	#Initialize unique node and publish to topic /turtle1/cmd_vel
	rospy.init_node('circle', anonymous='True')
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	#Set values to make turtlesim move in a circle
	vel_msg.linear.x = 2.0
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 1.8
	
	#Start loop publishing set values to turtlesim
	while not rospy.is_shutdown():
		
		velocity_publisher.publish(vel_msg)


#When program is called, run function and stop when user hits Ctrl^C
if __name__ == '__main__':
	try:
		move_circle()
		
	except rospy.ROSInterruptException: pass
