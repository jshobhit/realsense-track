import cv2
import os
import sys
import numpy as np

"""
class OptFlowTracker(object):

    def __init__(self, vidpath, roi = None):
        self.vid = cv2.VideoCapture(vidpath)
        self.orb = cv2.ORB_create()        

    def track(self):
        for idx, frame in enumerate(self.vid):
            self.vid[idx] = self.process_frame(frame)
    
    def process_frame(self, frame):

"""     

vid = cv2.VideoCapture('../images/bend/color/color.mp4')
orb = cv2.ORB_create()
# matcher = cv2.BFMatcher()
roi = [(819, 392), (1005, 563)]

def point_select(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        roi.append((x,y))
    elif event == cv2.EVENT_RBUTTONDOWN and len(roi) > 0:
        roi.pop()

def process_frame(img):
    out = img.copy()
    mask_img = np.zeros(out.shape).astype(np.uint8)
    pt1, pt2 = roi
    cv2.rectangle(mask_img, pt1, pt2, (255,255,255), -1)
    masked = cv2.bitwise_and(out, mask_img)
    corners = cv2.goodFeaturesToTrack(cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY), 20, 0.01, 10)     
    corners = np.int0(corners)
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(out, (x,y), 3, 255, -1)
    return out

# cv2.namedWindow('Output')
# cv2.setMouseCallback('Output', point_select)

while True:

    try:
        ret, frame = vid.read()
        out = process_frame(frame) if len(roi) == 2 else frame
        cv2.imshow('Output', out)
        key = cv2.waitKey(50)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        else:
            continue
    
    except AttributeError:
        print('No image found')
        break


