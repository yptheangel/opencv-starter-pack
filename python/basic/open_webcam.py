import cv2

# 0 is the representation of your camera, it starts from 0, number 1 is your second connected USB webcam
cap = cv2.VideoCapture(0)

# Videos are actually multiple frames processed frame-by-frame
while cap.isOpened():
    isSuccess, frame = cap.read()

    cv2.imshow('My webcam stream', frame)
    k = cv2.waitKey(1)
    # Press "Esc" key to exit program
    if k == 27:
        break

# Release the frames
cap.release()
# Destroy all windows
cv2.destroyAllWindows()
