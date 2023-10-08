import cv2

# read your picture and store into variable "img"
img = cv2.imread('picture.jpg')

# scale image down 3 times
for i in range(3):
    img = cv2.pyrDown(img)

    # save scaled image
    cv2.imwrite(f'picture_scaled_{i}.jpg', img)