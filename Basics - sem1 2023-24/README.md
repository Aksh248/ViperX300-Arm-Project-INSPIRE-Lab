This is the folder containing the work done in the first semester of 2023-24. The work in this sem primarily involved the basic understanding of the arm, initialising the origin and colour based pick and place of objects on the workspace.

-The Python libraries used for the same are:
Interbotix_xs_modules.arm - The arm SDK which allows us to work with the robot
Math - to do some basic operations like tan calculations for coordinates being fed to the arm
Imutils - to access the webcam/overhead camera
OpenCV (cv2) - for computer vision
Matplotlib.pyplot - to plot the images gotten from the Realsense Sensor
Pyrealsense2 - the SDK for the realsense sensor
Numpy - for matrix/image operations
Time - for execution speed calculations and for suggested speed of the robotic arm.

- Explanation of the various codes and their purposes in my project folder:
Camera_tracking_test.py - This  is a basic code that just finds an object of a specified colour in the frame and prints the coordinates of the geometric centre of the object. This is then converted to cm, from its original pixel value. This was modified from a pyimage search tutorial on basic object tracking. In the updated version, it finds the origin with the find_origin function then finds the coordinates of an object specified by colour wrt to the origin.
Arm movement.py - Has two different functions defined for the robotic arm, one for pick up and another for drop, that take in the coordinates of the object in the workspace as input and the arm moves to the required position and picks/drops the object based on the function called.
Find_obj.py - Does the basic function of picking up an object with a  fixed colour, which can be specified by the user.
Pickup_and_drop.py - takes user input of colour of object to pick up, and colour of where to drop it off and the arm will take the required object and drop it in the specified space.
Tracking_object.py - will track the position of the object and if the object remains in the same position for 2 or more loop iterations, the arm will pick up the object.
Aruco_detect.py - The code detects an Aruco code of a specified type and dimensions in the camera field of view, and marks its coordinates in the frame and shows the coordinates of the Aruco tag on the frame
Aruco_type.py - Finds the type of the Aruco Tag used in an image.
Distance.py - A pick and place application that doesn’t use the dynamic origin. (Pre-Midsem implementation of the pickup code)
Origin_finder.py - This code combines a MOSSE Tracker with an Aruco detection code, to detect and track the exact coordinates of an Aruco Marker in a frame. This helped to resolve the issue with the moving origin. As the marker is stationary wrt the origin, we can use this to calculate the origin in any situation.
colour_find.py- a code to find the threshold values in HSV for any specific colour. This was taken from a tutorial (referenced in the list of references section of the report)
Object_tracker.py - Implements a simple MOSSE tracker in which a user can select a segment of a frame to be tracked (followed a tutorial from pyimagesearch for the same - referenced in the end of the report)
