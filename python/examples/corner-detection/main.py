import cv2

# Load the image
image = cv2.imread('chessboard.jpg', cv2.IMREAD_GRAYSCALE)  # Load the image in grayscale

# Detect Harris corners
dst = cv2.cornerHarris(image, blockSize=5, ksize=3, k=0.1)
dst = cv2.dilate(dst, None)

# Define a threshold for considering a pixel as a corner
threshold = 0.07 * dst.max()

# Mark the corners on the image
image_with_corners = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image_with_corners[dst > threshold] = [0, 0, 255]  # Mark corners in red

# Display the image with marked corners
cv2.imshow('Harris Corners', image_with_corners)
cv2.waitKey(0)
cv2.destroyAllWindows()