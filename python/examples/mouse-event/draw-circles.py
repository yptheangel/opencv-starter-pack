import numpy as np
import cv2
import math

drawing = False # True if mouse is pressed
ix,iy = -1,-1

# Create a function based on a CV2 Event (Left button click)
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # Take note of where that mouse was located
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing == True
        
    elif event == cv2.EVENT_LBUTTONUP:
        radius = int(math.sqrt( ((ix-x)**2)+((iy-y)**2)))
        cv2.circle(img,(ix,iy),radius,(0,0,255), thickness=1)
        drawing = False

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# This names the window so we can reference it
cv2.namedWindow('image')

# Connects the mouse button to our callback function
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF # Press esc to quit
    if k == 27:
        break

cv2.destroyAllWindows()