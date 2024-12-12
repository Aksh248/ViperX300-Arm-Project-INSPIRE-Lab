#Live video stream code
import imagezmq
import numpy as np
import matplotlib.pyplot as plt
# initialize the ImageHub object
image_hub = imagezmq.ImageHub()
try:
    while True:
        # receive the image from the client
        (hostname, frame) = image_hub.recv_image()
        # display the image
        plt.imshow(frame)
        plt.close()
        image_hub.send_reply(b'OK')
except KeyboardInterrupt:
    print("Shutting down gracefully...")
finally:
    # cleanup
    image_hub.close() # Ensure the socket is closed