# client.py
from imutils.video import VideoStream
import imagezmq
import socket
import time
import imutils
import cv2
# construct the argument parser and parse the arguments


# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://localhost:5555")

# allow the camera sensor to warm up
time.sleep(2.0)

# start the video stream thread
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()

    # send the frame to the server
    sender.send_image(socket.gethostname(), frame)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
	
