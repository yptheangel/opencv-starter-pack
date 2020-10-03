import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('triangle.png')

    height, width, _ = img.shape

    cv2.circle(img, (223,41), 5, (0, 0, 255), -1)
    cv2.circle(img, (52, 302), 5, (0, 255, 0), -1)
    cv2.circle(img, (392, 302), 5, (255, 0, 0), -1)

    pts1 = np.float32([[223,41],[52, 302],[392, 302]])
    pts2 = np.float32([[223, 41], [123, 302], [323, 200]])

    M = cv2.getAffineTransform(pts1, pts2)
    output = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('raw', img)
    cv2.imshow('output', output)
    cv2.waitKey(0)