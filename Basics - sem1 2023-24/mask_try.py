# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import cv2
import imutils
import time

# define the lower and upper boundaries of the "color"
# ball in the HSV color space, then initialize the
# list of tracked points
colorLower = (0,152,38)
colorUpper = (5, 255,255)
pts = deque(maxlen=200)
# grab the reference
# to the webcam

vs = VideoStream(src=0).start()

# otherwise, grab a reference to the video 

frame = vs.read()
frame = imutils.resize(frame, width=600)
#x0,y0 = find_origin(frame)
# keep looping
count =0
while True:
	# grab the current frame
	frame = vs.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# construct a mask for the color "color", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, colorLower, colorUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	cv2.imshow("mask", mask)
	cv2.imwrite('mask.png',mask)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	time.sleep(1)
	
# if we are not using a video file, stop the camera video stream

vs.release()


cv2.destroyAllWindows()