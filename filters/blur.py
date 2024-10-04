import cv2

class BlurFilter:
    def apply(self, frame):
        return cv2.GaussianBlur(frame, (15, 15), 0)
