import cv2

# This example overlays a filled rectangle box on a camera frame

cap = cv2.VideoCapture(0)
face = cv2.imread("lena.jpg")

while cap.isOpened():
    isSuccess, frame = cap.read()

    if isSuccess:
        foreground = frame.copy()
        # topleft point consists of xmin = origin 0 ,ymin is 60% of ymax
        # bottomright point is xmax,ymax
        topleft_point = (0, int(frame.shape[0] * 0.6))
        bottomright_point = (frame.shape[1], frame.shape[0])
        w_overlay = bottomright_point[0] - topleft_point[0]
        h_overlay = bottomright_point[1] - topleft_point[1]

        foreground = cv2.rectangle(foreground, topleft_point, bottomright_point, (0, 255, 0), -1)
        overlayed = cv2.addWeighted(src1=foreground, alpha=0.3, src2=frame, beta=0.7, gamma=0)

        # paste the face image on overlayed image
        x_offset = 40
        y_offset = 40
        overlayed[topleft_point[1] + y_offset:topleft_point[1] + y_offset + face.shape[0],
        topleft_point[0] + x_offset:topleft_point[0] + x_offset + face.shape[1]] = face

        offset_from_pic_x = 50
        offset_from_pic_y = 60
        text_start_from_x = topleft_point[0] + x_offset + face.shape[1] + offset_from_pic_x
        text_start_from_y = topleft_point[1] + y_offset + offset_from_pic_y
        overlayed = cv2.putText(overlayed, "Lena", (text_start_from_x, text_start_from_y), cv2.FONT_HERSHEY_DUPLEX, 2,
                                (255, 255, 255),
                                2)

        cv2.imshow('My webcam stream', overlayed)
        k = cv2.waitKey(1)
        # Press "Esc" key to exit program
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
