# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import cv2
import imutils
import time
from origin_finder import find_origin

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
x0,y0 = find_origin(frame)
# keep looping
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

# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	cv2.drawContours(frame, cnts, -1, (0, 255, 0), 3) 
	
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid 
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	# update the points queue
	pts.appendleft(center)
	center2 = (center[0] -x0 , center[1]-y0)
	print(center2)
	cv2.circle(frame, (0,0), 4, (0, 0, 255), -1)
	cv2.circle(frame, (x0,y0), 4, (0, 0, 255), -1)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	time.sleep(1)
# if we are not using a video file, stop the camera video stream

vs.release()


cv2.destroyAllWindows()