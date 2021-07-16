# bag to videos

from rosbag.bag import Bag
import cv2
import os
import sys

bag = Bag(sys.argv[1]) if os.path.exists(sys.argv[1]) else None

ref_dict = {'/device_0/sensor_1/Color_0/image/data': 'color',
        '/device_0/sensor_0/Infrared_0/image/data': 'infra',
        '/device_0/sensor_0/Depth_0/image/data': 'depth',
        '/device_0/sensor_0/Confidence_0/image/data': 'confidence'}

top = {v:k for k,v in ref_dict.iteritems()}

if bag is not None:

    color_msgs = bag.read_messages(topics = top['color'])
    depth_msgs =  bag.read_messages(topics = top['depth'])
    infra_msgs = bag.read_messages(topics = top['depth'])
   
    print(list(map(len, [color_msgs, depth_msgs, infra_msgs])))

