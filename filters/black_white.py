import cv2

class BlackWhiteFilter:
    def apply(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
