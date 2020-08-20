#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_forward():
	
	rospy.init_node('forward', anonymous = 'True')
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	distance = int(input("Distance: "))
	
	vel_msg.linear.x = 1.0
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 0.0
	
	distance_travelled = 0
	t0 = rospy.Time.now().to_sec()
	
	while not rospy.is_shutdown():
		
		while (distance_travelled < distance):
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			distance_travelled = 1.0 * (t1 - t0)
	
		vel_msg.linear.x = 0.0
		velocity_publisher.publish(vel_msg)
		
if __name__ == '__main__':
	try:
		move_forward()
	
	except rospy.ROSInterruptException: pass
			
		
