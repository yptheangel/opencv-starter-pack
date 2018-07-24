#This is an example provided by OpenCV team and is included in the original OpenCV folder
#This sample code uses cascade classifiers to detect face and eyes

import cv2
import numpy as np

#loads the classifer file for eyes
eye_cascade = cv2.CascadeClassifier('../haarcascade_eye.xml')
#loads the classifer file for face
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

#Set program to read frames from webcam
cam = cv2.VideoCapture(0)

while cam.isOpened():
	ret , frame = cam.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)

	#print out the number of faces in the frame
	print "Number of faces: {0}".format(len(faces))

	#capture photo if there is more than 7 faces
	if len(faces)>8:
		cv2.imwrite("group_photo.jpg",frame)
		break
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_color = frame[y:y+h,x:x+w]
	
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+ey),(0,255,0),2)

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()

