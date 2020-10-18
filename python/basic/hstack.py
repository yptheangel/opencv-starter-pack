import cv2

if __name__ == '__main__':
    frame1 = cv2.imread("picture.jpg")
    frame2 = cv2.imread("picture.jpg")
    frames = [frame1, frame2]
    output = cv2.hconcat(frames)
    cv2.imshow("output", output)
    cv2.waitKey(0)