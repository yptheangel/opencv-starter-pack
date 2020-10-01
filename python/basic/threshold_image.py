import cv2

# read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

# Converting the image to greyscale.
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  
# Applying different thresholding techniques on the input image with 100 as a threshold value.

# cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
# cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
# cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.
# cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
# cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.
ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC) 
ret, thresh4 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO) 
ret, thresh5 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV) 
  
# The window showing output images with the corresponding thresholding techniques applied to the input images .
cv2.imshow('Threshold Binary', thresh1) 
cv2.imshow('Threshold Binary Inverted', thresh2) 
cv2.imshow('Truncated Threshold', thresh3) 
cv2.imshow('Set to 0', thresh4) 
cv2.imshow('Set to 0 Inverted', thresh5) 
    
# Destroy windows on keypress
print("Press any key to close the windows")
cv2.waitKey(0)
cv2.destroyAllWindows()  