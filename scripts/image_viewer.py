import cv2
import os
import sys

target = sys.argv[1]
images = [cv2.imread(target+f) for f in os.listdir(target)] if os.path.exists(target) else None

key = ''
idx = 0

while key is not ord('q'):

    cv2.imshow('output', images[idx])
    key = cv2.waitKey(1)
    
    if key == ord('a'):
        idx -= 1
    elif key == ord('d'):
        idx += 1

cv2.destroyAllWindows()

