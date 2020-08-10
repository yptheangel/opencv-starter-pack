import cv2

# using USB webcam number 1
cam = cv2.VideoCapture(0)

# You can save your video according to the same size as your webcam stream or hardcode the size you like
# frame_width = int(cam.get(3))
# frame_height = int(cam.get(4))
# recorder = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'),20, (frame_width,frame_height))

# Saving the video in 640x480 size
recorder = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (640, 480))

while cam.isOpened():
    # read the frames from the webcam
    ret, frame = cam.read()
    # save the frame and write to our output file
    recorder.write(frame)

    # show the frames in a Windows
    cv2.imshow('My Webcam', frame)
    k = cv2.waitKey(1) & 0xFF
    # if 'Q' is pressed, the programs exits
    if k == ord('q'):
        break

# release the webcam frames
cam.release()
# release the video recorder frames
recorder.release()
# destroy all windows
cv2.destroyAllWindows()
