import cv2
from threading import Thread


class CameraStream:
    def __init__(self, cam_index=0):
        self.cap = cv2.VideoCapture(cam_index)
        print(f"Video backend: {self.cap.getBackendName()}")

        self.isSuccess, self.frame = self.cap.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            self.isSuccess, self.frame = self.cap.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.cap.release()
        cv2.destroyAllWindows()
