import cv2
import os
import random

basepath = '../output/helical2/depth/'
img = cv2.imread(basepath+str(random.choice(os.listdir(basepath))))
print(img.shape)
cv2.namedWindow('output')
key = ''

while key != ord('q'):
    cv2.imshow('output', img)
    key = cv2.waitKey(1)

cv2.destroyAllWindows()

