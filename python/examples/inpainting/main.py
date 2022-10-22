import cv2
import numpy as np

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv2.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv2.imshow(self.windowname, self.dests[0])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None

        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, 5)
            self.dirty = True
            self.prev_pt = pt
            self.show()

img = cv2.imread('picture.jpg')

img_mark = img.copy()
mark = np.zeros(img.shape[:2], np.uint8)
sketch = Sketcher('img', [img_mark, mark], lambda : ((255, 255, 255), 255))

while True:
    ch = cv2.waitKey()
    if ch == 27:
        break
    if ch == ord(' '):
        res = cv2.inpaint(img_mark, mark, 3, cv2.INPAINT_TELEA)
        cv2.imshow('inpaint', res)
    if ch == ord('r'): # Press 'r' to generate inpaiting image
        img_mark[:] = img
        mark[:] = 0
        sketch.show()
cv2.destroyAllWindows()