import cv2

cam = cv2.VideoCapture(0)  # Use USB webcam first, if you have second webcam, change to 1 if necessary

# You can save your video according to the size as your webcam stream or hardcode the size you like
# Method 1
# frame_width, frame_height = int(cam.get(3)), int(cam.get(4))
# recorder = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))
# Method 2: Saving the video in 640x480 size
recorder = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (640, 480))

while cam.isOpened():
    ret, frame = cam.read()  # read the frames from the webcam
    # save the frame and write to our output file
    recorder.write(frame)
    cv2.imshow('My Webcam Stream', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):  # if 'Esc' or 'Q' key is pressed, the programs exits
        break

cam.release()  # release the webcam frames
recorder.release()  # release the video recorder frames
cv2.destroyAllWindows()  # destroy all windows
