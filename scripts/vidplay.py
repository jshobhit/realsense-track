import cv2
import sys

def preprocess(img):
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = cv2.normalize(img, dst = None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX)
        print(img.shape[2])
    # out = cv2.applyColorMap(img, cv2.COLORMAP_VIRIDIS)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return out

vid = cv2.VideoCapture(sys.argv[1])

# cv2.namedWindow('output')
# cv2.moveWindow('output', 900, -900)
# cv2.imshow('output', vid.read()[1])
# cv2.waitKey(1)

while vid.isOpened():
    ret, frame = vid.read()
    frame = preprocess(frame)
    cv2.imshow('output', frame)
    if cv2.waitKey(5) == ord('q'):
        break


