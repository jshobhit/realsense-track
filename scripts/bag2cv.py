# Rospy to display camera and actuator features.
# Read a settings.json or .yaml or even .pkl to apply certain parameters to an image feed and generate the instrumentation menu

import rospy
import os
import cv2
from rosbag.bag import Bag
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import sys

class FeedParser():

    def __init__(self, feed, params = None):

        self.bridge = CvBridge()
        self.rgb_mode = None
        self.img = None

        if feed.endswith('.bag'): 
            # For static bagfile interface
            bagfile = Bag(feed, 'r')
            self.color_msgs = [self.bridge.imgmsg_to_cv2(x) for x in bagfile.read_messages(topics = '/device_0/sensor_1/Color_0/image/data')]
            self.depth_msgs = [self.bridge.imgmsg_to_cv2(x) for x in bagfile.read_messages(topics = '/device_0/sensor_0/Deoth_0/image/data')]
            self.infra_msgs = [self.bridge.imgmsg_to_cv2(x) for x in bagfile.read_messages(topics = '/device_0/sensor_0/Infrared_0/image/data')]
            print(list(map, [self.color_msgs, self.depth_msgs, self.infra_msgs]))
        
        elif feed.endswith('data'):
            # For dynamic pub-sub interface
            if feed.split('/')[1] == 'sensor_1':
                rospy.Subscriber(feed, Image, self.rgb_parse)
                self.rgb_mode = True
            elif feed.split('/')[1] == 'sensor_0':
                rospy.Subscriber(feed, Image, self.mono_parse)
                self.rgb_mode = False
            else:
                print('Please check input feed\n\n{0}'.format(feed))
                self.rgb_mode = None

    def rgb_parse(self, data):
        self.rgb_img = self.bridge.imgmsg_to_cv2(data.data, encoding = 'bgr8')
        print('Apply pickled parameters here')
        self.img = cv2.cvtColor(self.rgb_img, cv2.COLOR_BGR2GRAY)

    def mono_parse(self, data):
        self.img = self.bridge.imgmsg_to_cv2(data.data, encoding = 'passthrough')
        print('Apply pickled parameters here')


if __name__ == "__main__":
    rospy.init_node('main', anonymous=False)
    fp = FeedParser(sys.argv[1])
    rospy.spin()
