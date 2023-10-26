import cv2
import numpy as np

img = cv2.imread('ball.jpg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5)

rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows/16, param1=150, param2=20, minRadius=1, maxRadius=40)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0,:]:
        center = (c[0], c[1])
        cv2.circle(img, center, 1, (0, 100, 100), 3)
        radius = c[2]
        cv2.circle(img, center, radius, (255,0,255),3)

cv2.imshow("Circles detected", img)
cv2.waitKey()