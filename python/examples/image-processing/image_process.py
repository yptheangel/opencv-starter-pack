import cv2

cam = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(500,16,True)

while cam.isOpened():
        ret, frame = cam.read()
        fgmask = fgbg.apply(frame)
        cv2.imshow('Original Frame',frame)
        #Display the frame after background subtraction
        cv2.imshow('After Background Subtraction',fgmask)
        #Display the frame after Edge Detection+BackgroundSubtraction
        edges = cv2.Canny(fgmask,100,200)
        cv2.imshow('After Edge Detection',edges)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
                break

cam.release()
cv2.destroyAllWindows()
