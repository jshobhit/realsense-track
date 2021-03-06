from rosbag.bag import Bag
import pandas as pd
from cv_bridge import CvBridge
import cv2
import numpy as np
import os

filepath = raw_input('Enter filepath:\n')

bridge = CvBridge()
print('Reading Bag file')
bag = Bag(filepath)
directory = os.path.dirname(filepath) 
print('Saving all output from {1} to directory: {1}'.format(filepath, directory))

if not os.path.exists(directory+'/output'):
    os.mkdir(directory+'/output')

def smart_write(img, direc, filename):
    if not os.path.exists(direc):
        os.mkdir(direc)
    cv2.imwrite('{0}/img_{1}.jpg'.format(direc, filename), img)

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
        try:
	    img = bridge.imgmsg_to_cv2(msg)
            smart_write(img, '{0}/output/depth'.format(directory), t)
        except:
            print('Error in depth')
            pass
    elif topic == topics['color']:
        try:
	    img = bridge.imgmsg_to_cv2(msg)
	    smart_write(img, '{0}/output/color'.format(directory), t)
        except:
            print('Error in color')
            pass
    elif topic == topics['infra']:
    	try:
            img = bridge.imgmsg_to_cv2(msg)
	    smart_write(img, '{0}/output/infra'.format(directory), t)	
        except:
            print('Error in infra')
            pass
    elif topic == topics['confidence']:
        try:
            img = bridge.imgmsg_to_cv2(msg)
	    smart_write(img,'{0}/output/confidence'.format(directory), t)	
        except:
            print('Error in conf')
            pass
    else:
	pass

print('Images extracted successfully')

