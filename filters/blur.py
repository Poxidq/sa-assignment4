import cv2

class BlurFilter:
    def apply(self, frame):
        return cv2.GaussianBlur(frame, (20, 20), 0)
