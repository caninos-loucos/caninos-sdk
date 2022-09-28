import cv2, logging


class Camera:
    def __init__(self, board):
        self.board = board

    def enable(self, device):
        logging.debug("Will enable camera.")
        self.device = device
        self.capture = cv2.VideoCapture(self.device)
        if self.capture.isOpened():
            self.board.register_enabled(self)
            width, height = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH), self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            logging.info(f"Labrador Camera initialized with dimensions: height = {height} width = {width}")
            return True

    def disable(self):
        logging.debug("Will disable camera.")
        self.capture.release()

    def get_dimensions(self):
        width, height = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH), self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return height, width

    def read(self):
        return self.capture.read()

    def save_frame(self, filename):
        ret, frame = self.read()
        if not ret:
            logging.error("Error reading frame.")
            return False

        cv2.imwrite(filename, frame)
        return True

    def __del__(self):
        logging.debug("Will release capture.")
        self.capture.release()

    def __repr__(self):
        return str({"device": self.device, "isOpened": self.capture and self.capture.isOpened() or False})
