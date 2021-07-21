# Rospy to display camera and actuator features.
# Read a settings.json or .yaml or even .pkl to apply certain parameters to an image feed and generate the instrumentation menu

import rospy
import os
import cv2
from rosbag.bag import Bag
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import sys
import numpy as np

class FeedParser():
    def __init__(self, feed, params = None):

        self.bridge = CvBridge()
        self.rgb_mode = None
        self.img = np.zeros((480, 640))
        if feed.endswith('.bag'): 
            # For static bagfile interface
            bagfile = Bag(feed, 'r')
            self.color_msgs = [self.bridge.imgmsg_to_cv2(x.message) for x in bagfile.read_messages(topics = '/device_0/sensor_1/Color_0/image/data')]
            self.depth_msgs = [self.bridge.imgmsg_to_cv2(x.message) for x in bagfile.read_messages(topics = '/device_0/sensor_0/Depth_0/image/data')]
            self.infra_msgs = [self.bridge.imgmsg_to_cv2(x.message) for x in bagfile.read_messages(topics = '/device_0/sensor_0/Infrared_0/image/data')]
            print(list(map(len, [self.color_msgs, self.depth_msgs, self.infra_msgs])))
        
        elif feed.endswith('data'):
            # For dynamic pub-sub interface
            if feed.split('/')[3] == 'Color_0':
                rospy.Subscriber(feed, Image, self.rgb_parse)
                self.rgb_mode = True
            elif feed.split('/')[3] == 'Depth_0' or 'Infrared_0':
                rospy.Subscriber(feed, Image, self.mono_parse)
                self.rgb_mode = False
            else:
                print('Please check input feed\n\n{0}'.format(feed))
                self.rgb_mode = None

    def rgb_parse(self, data):
        self.img = self.bridge.imgmsg_to_cv2(data,desired_encoding = 'bgr8')
        self.img = np.array(self.img)

    def mono_parse(self, data):
        self.img = self.bridge.imgmsg_to_cv2(data, desired_encoding = 'passthrough')
        self.img = cv2.normalize(self.img, self.img, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)



key = ''
if __name__ == "__main__":

    rospy.init_node('main', anonymous=False)
    
    rgb = FeedParser('/device_0/sensor_1/Color_0/image/data')
    depth = FeedParser('/device_0/sensor_0/Depth_0/image/data')
    infra = FeedParser('/device_0/sensor_0/Infrared_0/image/data')
    
    #out_img = np.hstack([rgb.img, depth.img])
    while key is not ord('q'):

        out_img = depth.img
        cv2.imshow('output', out_img)
        cv2.waitKey(1)
        rospy.spin()

    cv2.destroyAllWindows()

