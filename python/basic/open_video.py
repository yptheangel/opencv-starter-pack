import cv2

video = "yourvideo.mp4"
vcap = cv2.VideoCapture(video) # Change the name of video.mp4 to your filename

# A video is made of multiple frames, we process a video frame-by-frame
while True:
    isSuccess, frame = vcap.read()
    if not isSuccess:
        break
    else:
        cv2.imshow('My video stream', frame)
        k = cv2.waitKey(30) # 30 is the delay between frames, you can reduce it if you want your video to play faster
        if  k == 27 or k == ord('q'):  # Window will exit if 'Esc' or 'Q' key is pressed
            break

vcap.release() # Release the frames
cv2.destroyAllWindows() # Destroy all windows
