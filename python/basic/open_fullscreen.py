# OpenCV window in full screen

import cv2

camera = cv2.VideoCapture(0)
window_name = "Camera 0"

while camera.isOpened():
    success, frame = camera.read()
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, frame)

    # Press "Esc" key to exit program
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
