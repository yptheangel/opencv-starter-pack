import cv2

# Read image
img = cv2.imread('building.jpg', cv2.IMREAD_COLOR)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise in the image
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply laplacian filter
filtered_image = cv2.Laplacian(img, ksize=3, ddepth=cv2.CV_16S)

# Convert to uint8
filtered_image = cv2.convertScaleAbs(filtered_image)

cv2.imshow('original', img)
cv2.imshow('filtered', filtered_image)
cv2.waitKey(0)
