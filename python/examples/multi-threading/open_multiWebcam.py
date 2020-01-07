# an example to open 2 usb webcam using opencv python module
# caveat: since each thread will each produce 1 imshow window, user needs to manually close the window one at a time using "Esc" key
# author: yptheangel

import cv2
import threading

keyPressed = -1

print("OpenCV version: "+cv2.__version__)

def cameraThread1():
    #0 is the first camera
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame = cap.read()
        
        cv2.imshow('Camera 0',frame)
        keyPressed = cv2.waitKey(1)
        #the program will exit if 'Esc' key is pressed 
        if keyPressed == 27:
            break
    cap.release()
        

def cameraThread2():
    #1 is the second webcam
    cap1 = cv2.VideoCapture(1)

    while cap1.isOpened():
        _, frame1 = cap1.read()
        
        cv2.imshow('Camera 1',frame1)
        keyPressed = cv2.waitKey(1)

        if keyPressed == 27:
            break
    cap1.release()

t1 = threading.Thread(name='Thread1', target=cameraThread1)
t2 = threading.Thread(name='Thread2', target=cameraThread2)

t1.start()
t2.start()

#Destroy all windows
cv2.destroyAllWindows()

