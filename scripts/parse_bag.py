from rosbag.bag import Bag
import pandas as pd
from cv_bridge import CvBridge
import cv2
import numpy as np
import os

filename = raw_input('Enter filename:\n')

bridge = CvBridge()
print('Reading Bag file')
bag = Bag('./data/{}.bag'.format(filename))

def sample(x):
    pass

def proc_oflow(images):

    h, w = 720, 1280

    processed_images = []
    for image in images:
        hsv = np.zeros((h, w, 3), dtype=np.uint8)
        hsv[:, :, 0] = 255
        hsv[:, :, 1] = 255

        mag, ang = cv2.cartToPolar(image[..., 0], image[..., 1])
        hsv[..., 0] = int(ang*180/np.pi/2)
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

        processed_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        processed_images.append(processed_image)

    return np.stack(processed_images) 

ref_dict = {'/device_0/sensor_1/Color_0/image/data': 'color',
        '/device_0/sensor_0/Infrared_0/image/data': 'infra',
        '/device_0/sensor_0/Depth_0/image/data': 'depth',
        '/device_0/sensor_0/Confidence_0/image/data': 'confidence'}

topics  = {v:k for k,v in ref_dict.iteritems()}

for idx, data in enumerate(bag.read_messages()):
    topic, msg, t = data
    if topic == topics['depth']:
	img = bridge.imgmsg_to_cv2(msg, 'mono8')
	cv2.imwrite('./data/images/{0}/depth/img_{1}.jpg'.format(filename, t), img)
    elif topic == topics['color']:
	img = bridge.imgmsg_to_cv2(msg, 'bgr8')
	cv2.imwrite('./data/images/{0}/color/img_{1}.jpg'.format(filename, t), img)	
    elif topic == topics['infra']:
	img = bridge.imgmsg_to_cv2(msg)
	cv2.imwrite('./data/images/{0}/infra/img_{1}.jpg'.format(filename, t), img)	
    elif topic == topics['confidence']:
	img = bridge.imgmsg_to_cv2(msg)
	cv2.imwrite('./data/images/{0}/confidence/img_{1}.jpg'.format(filename, t), img)	
    else:
	pass

print('Images extracted successfully')
