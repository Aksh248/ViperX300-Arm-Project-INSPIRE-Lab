# import the necessary packages
from imutils.video import VideoStream
import argparse
import cv2
import imutils
import time
import math
#from arm_movement import pick_up, drop_off
from origin_finder import find_origin
# construct the argument parse and parse the arguments for the camera stream
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the colours
# of the objects in the HSV color space, then initialize the
# list of tracked points
colour_obj = input("enter object colour ")
if colour_obj =="red":
	colorLower = (0,152,38)
	colorUpper = (5, 255,255)
elif colour_obj =="yellow":
	colorLower = (26,129,162)
	colorUpper = (47, 255,137)
elif colour_obj =="green":
	colorLower = (42,106,68)
	colorUpper = (83, 255,255)
elif colour_obj =="blue":
	colorLower = (80,175,147)
	colorUpper = (179, 231,255)


vs = VideoStream(src=0).start()
time.sleep(1)

# grab the current frame
frame = vs.read()
# handle the frame from VideoCapture or VideoStream
frame = frame[1] if args.get("video", False) else frame
# if we are viewing a video and we did not grab a frame,
# then we have reached the end of the video
# resize the frame, blur it, and convert it to the HSV
# color space
frame = imutils.resize(frame, width=600)
x0,y0 = find_origin(frame)
print(x0,y0)

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
print(center)
xp = center[0]
yp = center[1]
colour = input("Enter drop off point colour ")
#convert pixels to cm and print that valuepink
xcm = (yp-342)*(0.00206)
ycm = (yp-491)*(0.00206)
center_cm = (xcm, ycm)
print(center_cm)
#pick_up(round(xcm,3), round(ycm,3))
if colour == "Pink" or colour == "pink":
    xd = 0.4
    yd = 0.025
elif colour == "Blue" or colour == "blue":
	xd = 0.04398
	yd = -0.3811
elif colour == "Yellow" or colour =="yellow":
	xd= 0.254
	yd = -0.381
elif colour == "Green" or colour == "green":
	xd = -0.04398
	yd = -0.44
elif colour == "White" or colour =="white":
	xd= -0.254
	yd = -0.381
yind = math.atan(yd/xd)
xind = math.sqrt((xd**2)+ (yd**2))-0.05
#yind = yind - 
#xind = xind -xin
#drop_off(xind, yind)
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
