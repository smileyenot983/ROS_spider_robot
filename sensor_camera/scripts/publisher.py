#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random


def talker():
	

	pub_cam = rospy.Publisher('/spider_robot/camera_joint_position_controller/command',Float64,queue_size=10)

	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(50)


	while not rospy.is_shutdown():
		
		positioncam = random.uniform(-0.5,0.5)	
		pub_cam.publish(positioncam)
		rate.sleep()



def main():
	talker()

if __name__ == '__main__':
	main()



