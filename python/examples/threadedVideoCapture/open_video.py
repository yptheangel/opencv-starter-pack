import cv2
import os
import sys

# Make sure you python module is within PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), "../../.."))
from python.examples.threadedVideoCapture.threaded_cam_stream import CameraStream

# Instantiate your threaded camera class
# cam_stream = CameraStream(r"C:\Users\ChooWilson\Desktop\koreacrowd.mp4")
cam_stream = CameraStream(0)
cam_stream.start()

while True:
    # read the frames from the camera stream running on another thread
    frame = cam_stream.read()
    cv2.imshow('My Webcam Stream', frame)
    k = cv2.waitKey(1)
    # if 'Q' is pressed the program will exits
    if k == ord('q'):
        break

# Stop the camera streamer thread
cam_stream.stop()
