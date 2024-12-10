# import the necessary packages
import cv2
import imutils
import time
import numpy as np
from PIL import Image
# define the lower and upper boundaries of the "color"
# ball in the HSV color space
colorLower = (45,92,139)
colorUpper= (90,255,255)
mask_generated = False
# Open the input video file



# grab the current frame
frame = np.array(Image.open('first_frame.jpg'))

# if the frame could not be grabbed, or if the mask has been generated for the first frame, then break

# resize the frame, blur it, and convert it to the HSV color space
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# construct a mask for the color "color", then perform
# a series of dilations and erosions to remove any small
# blobs left in the mask
mask = cv2.inRange(hsv, colorLower, colorUpper)


# Threshold the mask to ensure it contains only pixel values of 0 and 255
_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Display the mask
cv2.imshow("mask",mask)

# Save the mask with only pixel values of 0 and 1
mask[mask > 1] = 1
cv2.imwrite('~/Desktop/Arm_project/sem2/mask.png', mask)

# Set the flag indicating that the mask has been generated for the first frame
mask_generated = True





# close all windows
cv2.destroyAllWindows()