# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import cv2
import imutils
import time
#from arm_movement import pick_up
from interbotix_xs_modules.arm import InterbotixManipulatorXS
import math
from origin_finder import find_origin

# specifying name and type of arm
bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")

# define the lower and upper boundaries in HSV of the colour we wish to track
colourLower = (149,71,148)
colourUpper = (178, 255,255)

vs = VideoStream(src=0).start()
# grab the reference to the webcam
frame = vs.read()
frame = imutils.resize(frame, width=500)
#Find the present origin
x0,y0 = find_origin(frame)
#Previous origin
center_prev = (0,0)
time.sleep(1)
while True:
    # grab the current frame
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # construct a mask for the color, then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, colourLower, colourUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the object
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
    print(center)
    xp = center[0]
    yp = center[1]
    #convert pixels to cm and print that value
    xcm = (xp-x0)*(0.00206)
    ycm = (yp-y0)*(0.00206)
    center_cm = (xcm-center_prev[0], ycm-center_prev[1])
    print(center_cm)
    #finding requred x and angle for the arm
    yin = math.atan(center_cm[1]/center_cm[0])+0.025
    xin = math.sqrt((center_cm[0]**2)+ (center_cm[1]**2))-0.05
    print(xin, yin)
    #send the arm to current coordinates of the object
    bot.arm.set_ee_cartesian_trajectory(x=xin,z = 0.2)
    bot.arm.set_single_joint_position("waist",yin) 
    
    center_prev = center_cm
    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        bot.arm.go_to_home_pose()
        bot.arm.go_to_sleep_pose()
        break
# otherwise, release the camera
bot.arm.go_to_home_pose()
bot.arm.go_to_sleep_pose()
vs.release()
# close all windows
cv2.destroyAllWindows()