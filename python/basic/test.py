import cv2
import timeit
#Change the name of video.mp4 to your filename
#camera = cv2.VideoCapture('2017-06-26-165129_fullhd.webm')
camera = cv2.VideoCapture('2017-06-26-165129_fullhd.webm')
frame_number = 0 

#Videos are actually multiple frames processed frame-by-frame
while True:
	start_time = timeit.default_timer()
	ret, frame = camera.read()
	frame_number +=1
	elapsed_time = timeit.default_timer() - start_time
	FPS = (float(frame_number) / elapsed_time)
	print(FPS)
	cv2.imshow('My video stream',frame)
	k = cv2.waitKey(1) & 0xFF
	#if 'Q' is pressed the program will exits
	if k == ord('q'):
		break


#Release the frames
camera.release()
#Destroy all windows
cv2.destroyAllWindows()

