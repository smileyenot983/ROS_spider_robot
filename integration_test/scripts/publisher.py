#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random


def talker():



	pub111 = rospy.Publisher('/spider_robot/leg11_leg111_position_controller/command', Float64, queue_size=10)
	pub222 = rospy.Publisher('/spider_robot/leg22_leg222_position_controller/command', Float64, queue_size=10)
	pub333 = rospy.Publisher('/spider_robot/leg33_leg333_position_controller/command', Float64, queue_size=10)
	pub444 = rospy.Publisher('/spider_robot/leg44_leg444_position_controller/command', Float64, queue_size=10)




	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(50)


	while not rospy.is_shutdown():


		position111 = 0.2
		position222 = 0.1
		position333 = -0.1
		position444 = -0.2




		pub111.publish(position111)
		pub222.publish(position222)
		pub333.publish(position333)
		pub444.publish(position444)



		rate.sleep()



def main():
	talker()

if __name__ == '__main__':
	main()



