import cv2

# Read image
img = cv2.imread('building.jpg', cv2.IMREAD_COLOR)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply sobel filter in y and x direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

filtered_y = cv2.convertScaleAbs(sobel_y)
filtered_x = cv2.convertScaleAbs(sobel_x)

# Combine filtered image into single image
combined = cv2.addWeighted(filtered_x, 0.5, filtered_y, 0.5, 0)

cv2.imshow('original', img)
cv2.imshow('x direction', filtered_x)
cv2.imshow('y direction', filtered_y)
cv2.imshow('combined', combined)
cv2.waitKey(0)
