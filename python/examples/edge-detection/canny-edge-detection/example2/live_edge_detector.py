# example by "harshgtm01"
import cv2

cap = cv2.VideoCapture(0)                   # Device index in most cases is 0, try -1 if 0 does not work for you
                                            # if you have multiple cameras then you can use 1 for the second and 2 for the third camera as well

while True:                                 # In order to capture frame continuously
    _, frame = cap.read()                   # read method returns true or false depending upon whether the frame is available or not 
                                            # and stores it in frame variable if available
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)        # try changing the threshold values to get better result for your frames
    cv2.imshow("edges", edges)
    cv2.imshow("gray", gray)
    if cv2.waitKey(1) == ord("q"):          # press q in order to stop the program
        break

cap.release()
cv2.destroyAllWindows()
