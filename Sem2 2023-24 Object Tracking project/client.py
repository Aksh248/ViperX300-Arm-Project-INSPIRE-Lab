import cv2
import imagezmq
import socket
sender = imagezmq.ImageSender(connect_to='tcp://172.24.16.118:5555')

# Initialize the camera or video capture device
camera = cv2.VideoCapture(0)  # Change the argument to the appropriate device index or file path
device = socket.gethostname()
print(device)
while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture frame from camera.")
        break
    
    # Send the frame to the server
    #print("sending image")
    sender.send_image(device,frame)
    #print("Image sent")
    # Optionally display the frame (client-side)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

