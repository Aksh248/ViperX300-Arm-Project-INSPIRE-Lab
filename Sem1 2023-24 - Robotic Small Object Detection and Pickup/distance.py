# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
from arm_movement import pick_up
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping

# grab the current frame
frame = vs.read()
# handle the frame from VideoCapture or VideoStream
frame = frame[1] if args.get("video", False) else frame
# if we are viewing a video and we did not grab a frame,
# then we have reached the end of the video
# resize the frame, blur it, and convert it to the HSV
# color space
frame = imutils.resize(frame, width=600)
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
# construct a mask for the color "green", then perform
# a series of dilations and erosions to remove any small
# blobs left in the mask
mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

# find contours in the mask and initialize the current
# (x, y) center of the ball
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
center = None
# only proceed if at least one contour was found
if len(cnts) > 0:
	# find the largest contour in the mask, then use
	# it to compute the minimum enclosing circle and
	# centroid
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	# only proceed if the radius meets a minimum size
	for cnt in cnts:
		x1,y1 = cnt[0][0]
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		if len(approx) == 4:
			x, y, w, h = cv2.boundingRect(cnt)
			ratio = float(w)/h
			frame = cv2.drawContours(frame, [cnt], -1, (0,255,255), 3)
				
			# update the points queue
print(center)
xp = center[0]
yp = center[1]
#convert pixels to cm and print that value
xcm = (xp-70)*(1.2/273)
ycm = (yp)*(1.2/273)
center_cm = (xcm, ycm)
print(center_cm)
pick_up(ycm, xcm)
# show the frame to our screen
cv2.imshow("Frame", frame)
key = cv2.waitKey(1) & 0xFF
# if the 'q' key is pressed, stop the loop
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()
# otherwise, release the camera
else:
	vs.release()
# close all windows

cv2.destroyAllWindows()