This directory contains all the work done in the second semester of 2023-24. This part involved using models like XMem to segment and track objects.
All of the code for this project was written in Python, and done on an intel NuC system with Ubuntu 20.04 and ROS Noetic. In addition, the ML model is run on the server due the need to use a GPU.
The Python libraries used for the same are:
-Interbotix_xs_modules.arm - The arm SDK which allows us to work with the robot
-Math - to do some basic operations like tan calculations for coordinates being fed to the arm
-Imutils - to access the webcam/overhead camera
-OpenCV (cv2) - for computer vision
-Matplotlib.pyplot - To display the images in the jupyter notebook
-Time - for execution speed calculations and for suggested speed of the robotic arm.
-Imagezmq - A library that uses the ZeroMQ protocol for image processing applications
-PIL - An alternative to OpenCV for certain applications to open saved images from a folder
-Pytorch - to set model parameters for XMem and track objects with XMem
-Paramiko - An ssh related python library that helps with sending a file with the coordinate values from the server system to the local system

Explanation of the various codes and their purposes in my project folder:
- XMem_trial_final.py - The jupyter notebook that runs on the server and processes the images that are being sent from the local system. Most of the code is in this specific jupyter notebook
- first_frame.py - The code that runs locally, which sends an image of the first frame to generate the mask of the same.
- client.py - The code that runs locally to send frames constantly to the server, for constantly processing images
- obj_track.py - The code that takes the coordinates from a text file and feeds them to the arm, for the arm to track the object.
- mask.py - A python code that can be used to generate a mask of a specific object in a frame.
- sweep.py - A python code for the arm to perform a sweeping motion, for object segmentation.
- coordinates.txt - a text file that has the coordinates from the server
