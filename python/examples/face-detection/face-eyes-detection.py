# This is an example provided by OpenCV team and is included in the original OpenCV folder
# This sample code uses cascade classifiers to detect face and eyes

import cv2

# loads the classifer file for face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while cam.isOpened():
	isSuccess, frame = cam.read()
	display = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		#  output is in (xmin,ymin,w,h) and required coordinates are (xmin,ymin),(xmax,ymax)
		cv2.rectangle(display, (x, y), (x + w, y + h), (255, 0, 0), 2)
		# crop and get ROI for detected face
		roi_face = frame[y:y + h, x:x + w]

	cv2.imshow('frame', display)
	try:
		cv2.imshow('face',roi_face)
	except Exception as err:
		print(err)
	# Press "Esc" to close program
	if cv2.waitKey(1) & 0xFF == 27:
		break

cam.release()
cv2.destroyAllWindows()
