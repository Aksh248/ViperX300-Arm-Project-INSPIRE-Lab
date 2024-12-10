# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import math
from arm_movement import pick_up, drop_off
# construct the argument parse and parse the arguments

# define the lower and upper boundaries of the "color"
# ball in the HSV color space, then initialize the
# list of tracked points
colour_obj = input("enter obect colour")
if colour_obj =="purple":
	colorLower = (15,16,255)
	colorUpper = (179, 106,255)
elif colour_obj =="pink":
	colorLower = (149,71,148)
	colorUpper = (178, 255,255)
elif colour_obj =="green":
	colorLower = (71,62,221)
	colorUpper = (94, 117,255)
elif colour_obj =="blue":
	colorLower = (85,80,202)
	colorUpper = (128, 255,255)
# if a video path was not supplied, grab the reference
# to the webcam

vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
# allow the camera or video file to warm up
time.sleep(1)

# grab the current frame
frame = vs.read()
# handle the frame from VideoCapture or VideoStream
# if we are viewing a vi args.get("video", False) deo and we did not grab a frame,
# then we have reached the end of the video
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
# only proceed if at least one contour was found
if len(cnts) > 0:
	# find the largest contour in the mask, then use
	# it to compute the minimum enclosing circle and
	# centroid
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
print(center)
xp = center[0]
yp = center[1]
#convert pixels to cm and print that value
xcm = (517-xp)*(0.61/319)
ycm = (yp-198)*(0.00206)
yin = math.atan(ycm/xcm)+0.025
xin = math.sqrt((xcm**2)+ (ycm**2))
center_cm = (xcm, ycm)
center_cm = (xcm, ycm)
print(center_cm)
#(round(xcm,2), round(ycm,2))

# show the frame to our screen
cv2.imshow("Frame", frame)
key = cv2.waitKey(1) & 0xFF
# if the 'q' key is pressed, stop the loop
# if we are not using a video file, stop the camera video stream
vs.stop()

cv2.destroyAllWindows()