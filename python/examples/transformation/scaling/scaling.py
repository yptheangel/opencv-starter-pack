import cv2

if __name__ == '__main__':
    img = cv2.imread('cat.jpg')

    # resize image by 2 times
    img_resized_1 = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

    # Alternative
    # Resize image into 200x200
    img_resized_2 = cv2.resize(img, (200,200), interpolation = cv2.INTER_CUBIC)

    cv2.imshow('ras',img)
    cv2.imshow('resized_1', img_resized_1)
    cv2.imshow('resized_2', img_resized_2)
    cv2.waitKey(0)