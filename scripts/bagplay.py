import rospy
import sys
import os
import cv2
from cv_bridge import CvBridge

bridge = CvBridge()
rospy.init_node('main', anonymous = True)

class bagReader():

	def __init__(self, rgb_topic, depth_topic, infra_topic = None, conf_topic = None):
	
		self.bridge = CvBridge()
		rgb_sub = rospy.Subscriber(rgb_topic, Image, self.rgb_parse)
		depth_sub = rospy.Subscriber(depth_topic, Image, self.mono_parse)
		infra_sub = rospy.Subscriber(infra_topic, Image, self.mono_parse) if infra_topic is not None else None
		conf_sub = rospy.Subscriber(conf_topic, Image, self.mono_parse) if conf_topic is not None else None

	def rgb_parse(self, data):
		img = self.bridge.imgmsg_to_cv2(data.data, encoding = 'passthrough')
		self.img = img

	def mono_parse(self.data):
		img = self.bridge.imgmsg_to_cv2(data.data, encoding = 'passthrough')
		
