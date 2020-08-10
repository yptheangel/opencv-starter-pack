import cv2

# read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

# set the string of your text
myText = "Tomorrow is Saturday!"
# set the x,y coordinates of "Bottom Left of your text"
myCoordinates = (250, 100)
# insert the text into your frame
cv2.putText(frame, myText, myCoordinates, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(255, 0, 0),
            thickness=3)

# show your picture "frame" out as a GUI window
cv2.imshow('Hello World!', frame)

# waitkey is used to wait user's keypress, the number "0" is how long you wait before the next frame is read
k = cv2.waitKey(0)

# once any key is pressed, the window will be closed
cv2.destroyAllWindows()
