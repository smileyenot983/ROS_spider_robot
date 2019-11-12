#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random


def talker():
	pub11 = rospy.Publisher('/spider_robot/leg1_leg11_position_controller/command',Float64,queue_size=10)
	pub22 = rospy.Publisher('/spider_robot/leg2_leg22_position_controller/command',Float64,queue_size=10)
	pub33 = rospy.Publisher('/spider_robot/leg3_leg33_position_controller/command',Float64,queue_size=10)
	pub44 = rospy.Publisher('/spider_robot/leg4_leg44_position_controller/command',Float64,queue_size=10)
	pub111 = rospy.Publisher('/spider_robot/leg11_leg111_position_controller/command',Float64,queue_size=10)
	pub222 = rospy.Publisher('/spider_robot/leg22_leg222_position_controller/command',Float64,queue_size=10)
	pub333 = rospy.Publisher('/spider_robot/leg33_leg333_position_controller/command',Float64,queue_size=10)
	pub444 = rospy.Publisher('/spider_robot/leg44_leg444_position_controller/command',Float64,queue_size=10)

	pub_cam = rospy.Publisher('/spider_robot/camera_joint_position_controller/command',Float64,queue_size=10)

	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(50)


	while not rospy.is_shutdown():
		


		position11 = random.uniform(-1,1)
		position22 = random.uniform(-1,1)
		position33 = random.uniform(-1,1)
		position44 = random.uniform(-1,1)

		position111 = random.uniform(-0.5,0.5)
		position222 = random.uniform(-0.5,0.5)
		position333 = random.uniform(-0.5,0.5)
		position444 = random.uniform(-0.5,0.5)

		positioncam = random.uniform(-1,1)


		pub11.publish(position11)
		pub22.publish(position22)
		pub33.publish(position33)
		pub44.publish(position44)
		
		pub111.publish(position111)
		pub222.publish(position222)
		pub333.publish(position333)
		pub444.publish(position444)
	
		pub_cam.publish(positioncam)

		rate.sleep()


talker()
