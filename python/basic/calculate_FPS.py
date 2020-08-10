# Calculate FPS (Frames per second)

import cv2
from timeit import default_timer as timer

camera = cv2.VideoCapture(0)
frame_count = 0
total_time = 0

while camera.isOpened():
    start_time = timer()
    _, frame = camera.read()
    frame_count += 1
    elapsed_time = timer() - start_time
    total_time += elapsed_time

    FPS = float(frame_count / total_time)
    print(f"FPS: {FPS:.3f}")
    cv2.imshow('Webcam 0', frame)

    # Press "q" to exit program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the frames
camera.release()
# Destroy all windows
cv2.destroyAllWindows()
