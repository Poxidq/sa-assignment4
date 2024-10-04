import cv2

class VideoSource:
    def __init__(self, video_source=0):
        self.video_source = video_source
        self.capture = cv2.VideoCapture(self.video_source)

    def start(self, frame_queue):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            frame_queue.put(frame)

        self.capture.release()
