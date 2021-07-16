# bag to videos

from rosbag.bag import Bag
import yaml
import os
import sys

bagfile = Bag(sys.argv[1]) if os.path.exists(sys.argv[1]) else None
total_time = yaml.load(Bag(sys.argv[1])._get_yaml_info())['duration']

color_msgs = bagfile.read_messages(topics = '/device_0/sensor_1/Color_0/image/data')
depth_msgs = bagfile.read_messages(topics = '/device_0/sensor_0/Depth_0/image/data')
infra_msgs = bagfile.read_messages(topics = '/device_0/sensor_0/Infrared_0/image/data')

color_fps = len([x for x in color_msgs]) // total_time
depth_fps = len([x for x in depth_msgs]) // total_time
infra_fps = len([x for x in infra_msgs]) // total_time

print('Color FPS: {0}\n\nDepth FPS: {1}\n\nInfra FPS: {2}'.format(color_fps, depth_fps, infra_fps))

colorsavepath = raw_input('Enter the save path for the color feed')
print('Generating command for saving video')

cmd = 'rosrun image_view video_saver image:={0} --fps {1} --filename {2}'.format('/device_0/sensor_1/Color_0/image/data', color_fps, colorsavepath)
print(cmd)
