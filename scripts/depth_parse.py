import cv2
import os
import numpy as np

depth_imgs = [cv2.imread('./data/images/color/'+depth_img) for depth_img in os.listdir('./data/images/color')]
print('Number of depth images: '+str(len(depth_imgs)))
key = ''

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

cv2.namedWindow('out')
cv2.setMouseCallback('out', mouse_callback)
i = 0 
kernel = np.ones((3,3), np.uint8)

while key != ord('q'):
    if key == ord('a'):
        i += 1
    elif key == ord('d'):
        i -= 1
    try:
        img = cv2.equalizeHist(cv2.cvtColor(depth_imgs[i], cv2.COLOR_BGR2GRAY))
        ret, thresh = cv2.threshold(gray, 150, 220, 3)
        edges = cv2.Canny(thresh, 127, 200)
        contours, heir = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #[cv2.drawContours(depth_imgs[i], contour, 1, (0,255,0),1) for contour in contours if cv2.contourArea(contour) > 10]
        cv2.drawContours(img, contours, -1, (0,255,255), 1)
    except KeyError:
        print("Index out of bounds. Reseting to 0")
        i = 0
    
    cv2.imshow('out', img)
    key = cv2.waitKey(1)

cv2.destroyAllWindows()

