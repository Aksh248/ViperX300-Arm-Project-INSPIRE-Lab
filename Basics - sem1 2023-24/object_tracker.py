# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2

vs = VideoStream(src=0).start()
frame = vs.read()
print("[INFO] loading image...")

image = imutils.resize(frame, width=500)


# load the ArUCo dictionary, grab the ArUCo parameters, and detect
# the markers
print("[INFO] detecting '{}' tags...".format("DICT_ARUCO_ORIGINAL"))
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,
	parameters=arucoParams)

# verify *at least* one ArUco marker was detected
if len(corners) > 0:
	# flatten the ArUco IDs list
	ids = ids.flatten()
	# loop over the detected ArUCo corners
	for (markerCorner, markerID) in zip(corners, ids):
		# extract the marker corners (which are always returned in
		# top-left, top-right, bottom-right, and bottom-left order)
		corners = markerCorner.reshape((4, 2))
		(topLeft, topRight, bottomRight, bottomLeft) = corners
		# convert each of the (x, y)-coordinate pairs to integers
		topRight = (int(topRight[0]), int(topRight[1]))
		bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
		bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
		topLeft = (int(topLeft[0]), int(topLeft[1]))
		# draw the bounding box of the ArUCo detection
		cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
		cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
		cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
		cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
		# compute and draw the center (x, y)-coordinates of the ArUco
		# marker
		cX = int((topLeft[0] + bottomRight[0]) / 2.0)
		cY = int((topLeft[1] + bottomRight[1]) / 2.0)
		cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
		# draw the ArUco marker ID on the image
		cv2.putText(image, str(markerID),
			(topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (0, 255, 0), 2)
		print("[INFO] ArUco marker ID: {}".format(markerID))
		cv2.imshow("Image", image)
width = abs(topLeft[0] - topRight[0])
height = abs(-topLeft[1]+bottomLeft[0])
Center = (cX,cY)
tracker = cv2.TrackerMOSSE_create()
# initialize the bounding box coordinates of the object we are going
# to track
initBB = None
initBB = (bottomRight[0], bottomRight[1], width, width)
#print(initBB1)
frame = vs.read()
frame = imutils.resize(frame, width=500)
(H, W) = frame.shape[:2]
tracker.init(frame, initBB)
fps = FPS().start()
# otherwise, grab a reference to the video file
# initialize the FPS throughput estimator
# loop over frames from the video stream
while True:
	
	if initBB is not None:
		
		# grab the new bounding box coordinates of the object
		(success, box) = tracker.update(frame)
		print(box)
		#success = True
		# check to see if the tracking was a success
		if success:
			(x, y, w, h) = [int(v) for v in box]
			cv2.rectangle(frame, (x, y), (x - w, y - h),
				(0, 255, 0), 2)
		# update the FPS counter
		fps.update()
		fps.stop()
		# initialize the set of information we'll be displaying on
		# the frame
		info = [
			("Tracker", "mosse"),
			("Success", "Yes" if success else "No"),
			("FPS", "{:.2f}".format(fps.fps())),
		]
		# loop over the info tuples and draw them on our frame
		for (i, (k, v)) in enumerate(info):
			text = "{}: {}".format(k, v)
			cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
				cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	frame = vs.read()
	# check to see if we have reached the end of the stream
	if frame is None:
		break
	# resize the frame (so we can process it faster) and grab the
	# frame dimensions
	frame = imutils.resize(frame, width=500)
	(H, W) = frame.shape[:2]
	if key == ord("q"):
		break
# if we are using a webcam, release the pointer

vs.stop()

cv2.destroyAllWindows()