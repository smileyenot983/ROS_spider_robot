#!/usr/bin/env python
# license removed for brevity
import rospy

from control_msgs.msg import JointControllerState

import os





def main():
	counter = 0
	rospy.init_node('image_listener')

	#topics for each leg

	leg111_topic = '/spider_robot/leg11_leg111_position_controller/state'
	leg222_topic = '/spider_robot/leg22_leg222_position_controller/state'
	leg333_topic = '/spider_robot/leg33_leg333_position_controller/state'
	leg444_topic = '/spider_robot/leg44_leg444_position_controller/state'

	#2 subscribers for 2 legs

	rospy.Subscriber(leg111_topic,JointControllerState,check_position111)
	rospy.Subscriber(leg222_topic,JointControllerState,check_position222)
	rospy.Subscriber(leg333_topic,JointControllerState,check_position333)
	rospy.Subscriber(leg444_topic,JointControllerState,check_position444)


	rospy.spin()




def check_position111(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 11_111 passed test')


def check_position222(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 22_222 passed test')

def check_position333(msg):
	if abs(msg.set_point - msg.process_value) < 0.01:
		print('joint 33_333 passed test')
def check_position444(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 44_444 passed test')


if __name__ == '__main__':
	main()




