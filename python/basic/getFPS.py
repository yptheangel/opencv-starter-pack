#Manually calculating FPS

import cv2
import timeit
camera = cv2.VideoCapture(0)
frame_number = 0 

#Videos are actually multiple frames processed frame-by-frame
while camera.isOpened():
	start_time = timeit.default_timer()
	_, frame = camera.read()
	frame_number +=1
	elapsed_time = timeit.default_timer() - start_time
	FPS = (float(frame_number) / elapsed_time)
	print("FPS: "+FPS)
	cv2.imshow('Webcam 0',frame)
	k = cv2.waitKey(1)
	#if 'Q' is pressed the program will exits
	if k == ord('q'):
		break

#Release the frames
camera.release()
#Destroy all windows
cv2.destroyAllWindows()

