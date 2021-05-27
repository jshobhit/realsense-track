import cv2
import os
import sys
import numpy as np

vidpath_default = '../image/bend/color/color.mp4'

class OptFlowTracker(object):

    def __init__(self, vidpath, roi = None):
        try:
            self.vid = cv2.VideoCapture(vidpath)
        except FileNotFoundError:
            self.vid = cv2.VideoCapture(0)
        _, self.static_img = self.vid.read()
        self.orb = cv2.ORB_create()        
        self.roi = roi if roi is not None else []
        self.draw = False

        cv2.namedWindow('Output')
        cv2.setMouseCallback('Output', self.point_select)

    def point_select(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.roi.append((x,y))
            self.draw = True
        elif event == cv2.EVENT_RBUTTONDOWN and len(self.roi) > 0:
            self.roi.pop()
        elif event == cv2.EVENT_MOUSEMOVE and self.draw is True:
            pt1 = self.roi[0]
            pt2 = (x,y)
            cv2.rectangle(self.static_img, pt1, pt2, (200, 0, 0), -1)

    def process_frame(self, img):
        out = img.copy()
        mask_img = np.zeros(out.shape).astype(np.uint8)
        
        if self.roi is not None and len(self.roi) == 2:
            pt1, pt2 = self.roi
            cv2.rectangle(mask_img, pt1, pt2, (255,255,255), -1)
            masked = cv2.bitwise_and(out, mask_img)
            corners = cv2.goodFeaturesToTrack(cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY), 20, 0.01, 10)     
            corners = np.int0(corners)
            for corner in corners:
                x,y = corner.ravel()
                cv2.circle(out, (x,y), 3, 255, -1)
            return out

        else:
            return self.static_img

# matcher = cv2.BFMatcher()
# opt = OptFlowTracker('../images/bend/color/color.mp4', roi = [(819, 392), (1005, 563)])

if len(sys.argv) == 2:
    opt = OptFlowTracker(sys.argv[1])
else:
    opt = OptFlowTracker(vidpath_default)

while True:
    try:
        ret, frame = opt.vid.read()
        out = opt.process_frame(frame)
        cv2.imshow('Output', out)
        key = cv2.waitKey(50)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        else:
            continue
    except AttributeError:
        print('Attribute Error')
        break        

