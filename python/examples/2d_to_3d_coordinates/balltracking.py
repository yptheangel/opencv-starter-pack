import cv2
import numpy as np

calibration_data = np.load('/home/sudeesh/Technocrats/Task1/calibration_data.npz')
camera_matrix = calibration_data['mtx']
dist_coeffs = calibration_data['dist']
object_radius = 10 #assuming that we know the ball radius

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()

    if not ret:
        break

    undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)
    gray_frame = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_frame, (9, 9), 2)
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=50, param2=40, minRadius=2, maxRadius=30
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x, y, r = circle
            cv2.circle(undistorted_frame, (x, y), r, (0, 255, 0), 4)
            depth = (object_radius * camera_matrix[0, 0]) / (2 * r)
            
            print(f"X: {x}, Y: {y}, Z: {depth}")
 
    cv2.imshow("Ball Tracking", undistorted_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
