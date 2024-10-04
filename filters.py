import cv2

class BlackWhiteFilter:
    def apply(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

class MirrorFilter:
    def apply(self, frame):
        return cv2.flip(frame, 1)

class ResizeFilter:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def apply(self, frame):
        return cv2.resize(frame, (self.width, self.height))

class BlurFilter:
    def apply(self, frame):
        return cv2.GaussianBlur(frame, (15, 15), 0)

class FilterPipeline:
    def __init__(self, filters):
        self.filters = filters

    def apply(self, frame):
        for filter_obj in self.filters:
            frame = filter_obj.apply(frame)
        return frame
