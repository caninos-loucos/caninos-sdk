import cv2, logging, queue, time, threading


class Camera:
    def __init__(self, board):
        self.board = board
        self.capture = None
        self.low_fps_mode = True
        self.unbuffer_thread_running = False

    def enable(self, device, low_fps_mode=True):
        logging.debug(f"Will enable the camera at device {device}.")
        self.device = device
        self.capture = cv2.VideoCapture(self.device)

        if self.capture.isOpened():
            self.board.register_enabled(self)
            self._setup_low_fps_workaround(low_fps_mode)
            width, height = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH), self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            logging.debug(f"Labrador Camera initialized with dimensions: height = {height} width = {width}")
            return True

    def _setup_low_fps_workaround(self, low_fps_mode):
        """
        This is a workaround to the following:
        - When the consuming side has a low FPS, `cv2.read()` will not return the _latest_ frame, but a
          buffered one instead, which makes the result look really unresponsive.
        - With this workaround, we discard buffered ones and always get the latest frame.
        """
        self.low_fps_mode = low_fps_mode
        if self.low_fps_mode:
            logging.debug("NOTE: using low fps mode! (will use extra thread+queue to discard buffered frames)")
            self.q = queue.Queue()
            self.start_unbuffer_thread()

    def disable(self):
        logging.debug("Will disable camera.")
        if self.low_fps_mode:
            self.stop_unbuffer_thread()
        if self.capture:
            self.capture.release()

    def get_dimensions(self):
        width, height = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH), self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return height, width

    def read(self):
        if self.low_fps_mode:
            return True, self.q.get()
        else:
            return self.capture.read()

    def save_frame(self, filename):
        ret, frame = self.read()
        if not ret:
            logging.error("Error reading frame.")
            return False

        cv2.imwrite(filename, frame)
        return True

    def __del__(self):
        self.disable()

    def __repr__(self):
        return str({"device": self.device, "isOpened": self.capture and self.capture.isOpened() or False})

    def stop_unbuffer_thread(self):
        if self.unbuffer_thread_running:
            self.unbuffer_thread_running = False
            self.unbuffer_thread.join()

    def start_unbuffer_thread(self):
        self.unbuffer_thread = threading.Thread(target=self.unbuffer_reader)
        self.unbuffer_thread_running = True
        self.unbuffer_thread.start()

    # read frames as soon as they are available, keeping only most recent one
    def unbuffer_reader(self):
        logging.debug("The thread to handle low FPS consumers has started.")
        while self.unbuffer_thread_running:
            if not self.capture:
                time.sleep(1)
                continue
            ret, frame = self.capture.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()  # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)
        logging.debug("The thread to handle low FPS consumers has stopped.")
