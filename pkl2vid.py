import pandas as pd
import cv2
import numpy as np
import os

def click_callback(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Point: {}'.format((x,y)))

def sample(x):
    pass

key = ''

mode = raw_input('Enter the image mode you wish to see\n> depth\n> color\n> infra\n> confidence\n>>') # For python 2
#mode = str(input('Enter the image mode you wish to see\n> depth\n> color\n> infra\n> confidence\n>>')) # For python 3

images = [cv2.imread('./data/images/{0}/{1}'.format(mode, x)) for x in os.listdir('./data/images/{0}/'.format(mode))]

cv2.namedWindow('video')
cv2.createTrackbar('Frame', 'video', 0, len(images), sample)
cv2.setMouseCallback('video', click_callback)

while True:
    frame = cv2.getTrackbarPos('Frame', 'video')
    img = images[frame]
    #img = cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
    #img = cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN)

    cv2.imshow('video', img)
    key = cv2.waitKey(1)

    if key == 27: break

