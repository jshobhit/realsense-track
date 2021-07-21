import cv2
import sys

def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

vid = cv2.VideoCapture(sys.argv[1])

while vid.isOpened():
    ret, frame = vid.read()
    frame = preprocess(frame)
    cv2.imshow('output', frame)
    if cv2.waitKey(1) == ord('q'):
        break


