import cv2

# Change the name of video.mp4 to your filename
camera = cv2.VideoCapture('video.mp4')

# Videos are actually multiple frames processed frame-by-frame
while True:
    _, frame = camera.read()

    cv2.imshow('My video stream', frame)
    k = cv2.waitKey(1)
    # if 'Q' is pressed the program will exits
    if k == ord('q'):
        break

# Release the frames
camera.release()
# Destroy all windows
cv2.destroyAllWindows()
