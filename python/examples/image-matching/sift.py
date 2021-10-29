import cv2

# loading image
logo = cv2.imread('starbucks-logo.jpg')
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

img = cv2.imread('starbucks.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# keypoints
sift = cv2.SIFT_create()

# extract sift keypoints and descriptors
logo_keypoints, logo_descriptors = sift.detectAndCompute(logo_gray, None)
img_keypoints, img_descriptors = sift.detectAndCompute(img_gray, None)

# draw keypoints on logo
logo_keypoints_img = cv2.drawKeypoints(logo_gray, logo_keypoints, logo)

# feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(logo_descriptors, img_descriptors)
matches = sorted(matches, key=lambda x: x.distance)

matched_output = cv2.drawMatches(
    logo, logo_keypoints, img, img_keypoints, matches[:50], img, flags=2)

cv2.imshow("logo keypoints", logo_keypoints_img)
cv2.imshow("results", matched_output)
cv2.waitKey(0)
