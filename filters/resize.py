import cv2

class ResizeFilter:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def apply(self, frame):
        return cv2.resize(frame, (self.width, self.height))
