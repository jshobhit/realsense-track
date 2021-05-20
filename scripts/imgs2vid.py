import cv2
import os
import sys

filepath = sys.argv[1] 
image_paths = [os.path.join(filepath, file) for file in os.listdir(filepath)]
savepath = os.path.join(filepath, filepath.split('/')[-1]+'.mp4')

if os.path.exists(savepath):
	print('Over riding existing file')

h, w = cv2.imread(image_paths[0]).shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(savepath, fourcc, 1.0, (w,h))

for idx, path in enumerate(image_paths):
	frame = cv2.imread(path)
	cv2.imshow('video output', frame)
	cv2.waitKey(40)
	out.write(frame)

print('Saving file to {}'.format(savepath))
out.release()
cv2.destroyAllWindows()
