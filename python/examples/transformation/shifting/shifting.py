import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('cat.jpg')

    height, width, _ = img.shape

    # shift 20 to the right and 50 to the bottom
    M = np.float32(
        [
            [1, 0, 20],
            [0, 1, 50]
        ])
    output = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('raw', img)
    cv2.imshow('image_shifted', output)
    cv2.waitKey(0)