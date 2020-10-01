import cv2
import numpy as np

# Image translation example
if __name__ == '__main__':
    img = cv2.imread('cat.jpg')

    height, width, _ = img.shape

    # shift the image 20 pixels to the right and 50 pixels to the bottom
    M = np.float32(
        [
            [1, 0, 20],
            [0, 1, 50]
        ])
    output = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('raw', img)
    cv2.imshow('image_shifted', output)
    cv2.waitKey(0)
