import cv2
import numpy as np
import sys, os

def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

cv2.namedWindow('image explorer')
cv2.setMouseCallback('image explorer', on_click)

fourcc = cv2.VideoWriter_fourcc(*'x264')

filepath = sys.argv[1] if len(sys.argv) > 0 else None
imgs = [cv2.imread(os.path.join(filepath, file)) for file in os.listdir(filepath) if file.endswith('.jpg')] if filepath is not None else []

out = cv2.VideoWriter('./output.mp4', fourcc, 25, (imgs[0].shape[:2]))
[out.write(img) for img in imgs]

out.release()

print(['Success' if os.path.exists('./output.mp4') else 'Unsuccessful'])
    

