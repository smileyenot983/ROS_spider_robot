#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import getpass

user = getpass.getuser()

import os



bridge = CvBridge()


def main():
	counter = 0
	rospy.init_node('image_listener')

	image_topic = '/spider_robot/camera1/image_raw'
	rospy.Subscriber(image_topic,Image,image_callback)


	rospy.spin()
counter = 0

def increment():
	global counter
	counter=counter+1

def image_callback(msg):

	path = '/home/'+str(user)+'/robot_ws/src/sensor_camera/images/pic' + str(counter) + '.png'

	cv2_img = bridge.imgmsg_to_cv2(msg, 'mono8')

	cv2.imwrite(path,cv2_img)
	increment()
	print(counter)
	print(user)

if __name__ == '__main__':
	main()




