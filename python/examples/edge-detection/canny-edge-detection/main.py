import cv2


def CannyThreshold(threshold):
    # Perform bluring to reduce noise in the image
    img_blur = cv2.blur(img, (3, 3))
    # Apply canny edge filtering on blurred image
    detected_edges = cv2.Canny(
        img_blur, threshold, threshold*2, L2gradient=True)
    
    mask = detected_edges != 0
    dst = img * (mask[:, :, None].astype(img.dtype))
    cv2.imshow("Building", dst)


img = cv2.imread('building2.jpg')

cv2.namedWindow("Building")
cv2.imshow('Original Image', img)
cv2.createTrackbar('Thresholds:', "Building", 0, 100, CannyThreshold)

cv2.waitKey(0)
