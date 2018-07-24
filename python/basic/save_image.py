import cv2

#0 is the representation of your camera, it starts from 0, number 1 is your second connected USB webcam
camera = cv2.VideoCapture(0)

#Videos are actually multiple frames processed frame-by-frame
while True:
	ret, frame = camera.read()
	
	cv2.imshow('My webcam stream',frame)
	k = cv2.waitKey(1) & 0xFF
	#if 'Q' is pressed the program will exits
	if k == ord('q'):
		break
	elif k == ord('s'):
		#When 'S' is pressed, the current frame will be saved
		cv2.imwrite('my_picture.jpg',frame)

#Release the frames
camera.release()
#Destroy all windows
cv2.destroyAllWindows()

