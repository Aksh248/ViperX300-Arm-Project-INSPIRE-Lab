# import the necessary packages
from imutils.video import VideoStream
import cv2
import time
import imutils

def find_origin(image):
        # load the ArUCo dictionary, grab the ArUCo parameters, and detect
        # the markers
    print("[INFO] detecting '{}' tags...".format("DICT_ARUCO_ORIGINAL"))
    arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    arucoParams = cv2.aruco.DetectorParameters()
    detector= cv2.aruco.ArucoDetector(arucoDict, arucoParams)
    (corners, ids, rejected) = detector.detectMarkers(image)
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

            width = abs(topLeft[0] - topRight[0])
            height = abs(-topLeft[1]+bottomLeft[0])
            print(cX,cY)

            x0 = abs((0.20/0.00206) + (cX))
            y0 = abs((0.425/0.00206) + (cY))
            print("Pixel center", x0, y0)
            center2= (round(x0),round(y0))
            print(center2)
            cv2.circle(image, center2, 4, (0, 0, 255), -1)
            cv2.imshow("Frame",image)
    return center2
