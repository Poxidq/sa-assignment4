import cv2

class Display:
    def __init__(self):
        pass

    def start(self, frame_queue):
        while True:
            frame = frame_queue.get()
            if frame is None:
                break
            cv2.imshow('Processed Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
