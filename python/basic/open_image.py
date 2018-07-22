import cv2

#read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

#show your picture "frame" out as a GUI window
cv2.imshow('Hello World!', frame)

#waitkey is used to wait user's keypress, the number "0" is how long you wait before the next frame is read
k = cv2.waitKey(0)

#once any key is pressed, the window will be closed
cv2.destroyAllWindows()
