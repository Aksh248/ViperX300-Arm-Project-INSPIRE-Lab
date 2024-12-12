import requests
import cv2

# Specify the URL of the Flask server endpoint
url = 'http://localhost:5000/stream'  # Replace 'localhost:5000/stream' with the actual server URL

# Read the video file from disk or capture from camera
# You can use cv2.VideoCapture() to capture from camera or read from a video file
# cap = cv2.VideoCapture('video.mp4')

# OpenCV video capture object
cap = cv2.VideoCapture(0)  # Use the appropriate camera index or video file path

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from video stream.")
        break

    # Encode the frame as JPEG image
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()

    # Send the frame to the server for processing
    files = {'video': ('frame.jpg', img_bytes)}
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print('Frame processed successfully.')
    else:
        print('Failed to process frame. Status code:', response.status_code)

    # Optionally add a delay to control the frame rate (e.g., 1 frame per second)
    # Adjust the delay based on your desired frame rate
    cv2.waitKey(1000)

# Release the video capture object
cap.release()
