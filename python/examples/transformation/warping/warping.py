import cv2
import numpy as np

# read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

# selecting points for transformation. make sure these numbers falls under the dimensions of your image.
p1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
p2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]]) 

# generating transformation matrix
matrix = cv2.getPerspectiveTransform(p1, p2) 
# getting final results
result = cv2.warpPerspective(frame, matrix, (500, 600))

# displaying original and transformed image
cv2.imshow('Original', frame)
cv2.imshow('Warped', result)

# waiting for a key to be pressed
cv2.waitKey(0)
# destroying all windows
cv2.destroyAllWindows() 