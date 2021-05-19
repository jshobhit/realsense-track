import cv2
import os
import sys

filepath = sys.argv[1] 
image_paths = [os.path.join(filepath, file) for file in os.listdir(filepath)]

h, w, _ = cv2.imread(image_paths[0]).shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('../output.mp4', fourcc, 20.0, (w,h))

for path in image_paths:
	frame = cv2.imread(path)
	out.write(frame)

out.release()

vid = cv2.VideoCapture('../output.mp4')

while True:
	ret, frame = vid.read()
	print(frame.shape)
	cv2.imshow('out', frame)
	key = cv2.waitKey(1)

	if key == ord('q'):
		break
	else:
		continue

vid.release()
cv2.destroyAllWindows()
