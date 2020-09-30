import cv2

# read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

# display the image
cv2.imshow('My Image', frame) 

# Closes the image when the pressed key is 'q'
# 1. cv2.waitKey(0) waits for a key to be pressed.
#    When a key is pressed it returns the corresponding 32-bit integer value.
# 2. ord('q') returns the unicode value of 'q' which is 113.
print("Press 'q' to quit")
flag = True
while flag:
    if cv2.waitKey(0) == ord('q'):  
        cv2.destroyAllWindows()  
        flag = False