import cv2

if __name__ == '__main__':
    img = cv2.imread('hamster.jpg')

    height, width, _ = img.shape

    # set center of rotation as the center of image
    center_of_rotation = (width//2, height//2)
    cv2.circle(img, center_of_rotation, 5, (0, 0, 255), -1)

    rotation_degree = 45
    M = cv2.getRotationMatrix2D(center_of_rotation, rotation_degree, 1)
    output = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('raw', img)
    cv2.imshow('image_rotated', output)
    cv2.waitKey(0)