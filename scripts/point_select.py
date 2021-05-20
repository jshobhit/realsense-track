import cv2
import numpy as np

points = []
key = ''

def callback(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        print(x,y)

cv2.namedWindow('out')
cv2.setMouseCallback('out', callback)

while True:
    img = cv2.imread('./data/images/color/img_163.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127,255,0)
    cnt, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [cv2.drawMarker(image, pt, (0,255,0)) for pt in points]
    cv2.imshow('out', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

