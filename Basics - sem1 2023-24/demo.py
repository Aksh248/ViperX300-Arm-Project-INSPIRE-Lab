
import math
from arm_movement import pick_up, drop_off



# define the lower and upper boundaries of the colours
# of the objects in the HSV color space, then initialize the
# list of tracked points
colour_obj = input("enter pickup location colour ")
if colour_obj == "Pink" or colour_obj == "pink":
    xd = 0.4
    yd = 0
elif colour_obj == "Blue" or colour_obj == "blue":
	xd = 0.04398
	yd = -0.3811
elif colour_obj == "Yellow" or colour_obj =="yellow":
	xd= 0.254
	yd = -0.381
elif colour_obj == "Green" or colour_obj == "green":
	xd = -0.04398
	yd = -0.44
elif colour_obj == "White" or colour_obj =="white":
	xd= -0.254
	yd = -0.381

colour = input("Enter drop off point colour ")
center_cm = (xd,yd)
print(center_cm)
pick_up(xd,yd)
if colour == "Pink" or colour == "pink":
    xd = 0.4
    yd = 0
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
drop_off(xind, yind)
# show the frame to our screen

# if the 'q' key is pressed, stop the loop