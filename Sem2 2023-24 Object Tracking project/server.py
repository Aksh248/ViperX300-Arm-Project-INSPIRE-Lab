# server.py
import imagezmq
import cv2
import numpy as np

# initialize the ImageHub object
image_hub = imagezmq.ImageHub()

while True:
    # receive the image from the client
    (hostname, frame) = image_hub.recv_image()

    # display the image
    cv2.imshow("Image from {}".format(hostname), frame)
    cv2.waitKey(1)

# cleanup
cv2.destroyAllWindows()
