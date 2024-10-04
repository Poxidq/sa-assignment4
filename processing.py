import cv2
import numpy as np

class BnWFilter:
    def __init__(self, outputs=[], use_opencv=True):
        """
        Initialize the filter.
        :param outputs: List of functions to pass the processed frame to.
        :param use_opencv: If True, use cv2.cvtColor. If False, use manual grayscale formula.
        """
        self.outputs = outputs
        self.use_opencv = use_opencv

    def input(self, frame):
        data = frame.get_data()
        
        if self.use_opencv:
            # Use OpenCV for grayscale conversion
            data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        else:
            # Use manual formula for grayscale conversion
            coeffs = np.array([0.114, 0.587, 0.299])
            data = (data.astype(np.float32) * coeffs).sum(axis=-1)
            data = data.astype(np.uint8)  # Convert back to uint8 format

        frame.set_data(data)

        # Pass the frame to the next filter or output
        for output in self.outputs:
            output(frame)

class MirrorFilter:
    def __init__(self, outputs=[]):
        self.outputs = outputs

    def input(self, frame):
        frame.set_data(cv2.flip(frame.get_data(), 1))
        for output in self.outputs:
            output(frame)

class ResizeFilter:
    def __init__(self, outputs=[], scale=0.5):
        self.outputs = outputs
        self.scale = scale

    def input(self, frame):
        data = frame.get_data()
        width = int(data.shape[1] * self.scale)
        height = int(data.shape[0] * self.scale)
        frame.set_data(cv2.resize(data, (width, height)))
        for output in self.outputs:
            output(frame)

class EdgeFilter:
    def __init__(self, outputs=[]):
        self.outputs = outputs

    def input(self, frame):
        data = frame.get_data()

        # Check if the image is already grayscale
        if len(data.shape) == 3 and data.shape[2] == 3:
            gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        else:
            gray = data  # The frame is already grayscale

        frame.set_data(cv2.Canny(gray, 100, 200))
        for output in self.outputs:
            output(frame)

class SaveFilter:
    def __init__(self, outputs=[]):
        self.outputs = outputs

    def input(self, frame):
        # You can implement saving here if needed, for now it just passes the frame along
        for output in self.outputs:
            output(frame)
