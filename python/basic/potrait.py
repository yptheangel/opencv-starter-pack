import cv2

# Remember to rotate your camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    isSuccess, frame = cap.read()
    rotated = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('My webcam stream', rotated)

    # Press 'Esc' to quit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
