import cv2
import numpy as np
import rosbag

cap = cv2.VideoCapture('./data/bend.bag')
cv2.namedWindow("out", cv2.WINDOW_AUTOSIZE)

idx = 0
while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow("out", frame)
    key = cv2.waitKey(0)
    while key not in [ord('q'), ord('k')]:
        key = cv2.waitKey(0)
        print("Frame number: {}".format(idx))
    if key == ord('q'):
        break
    idx+= 1

cv2.destroyAllWindows()

