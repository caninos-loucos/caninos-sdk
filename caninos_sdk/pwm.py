import threading, timeit, logging


class PWM:
    freq = 0
    duty_cycle = 0
    period_high = 0
    period_low = 0
    thread: any
    gpio: any
    running: bool

    def __init__(self, gpio, freq, duty_cycle):
        self.gpio = gpio
        self.freq = freq
        self.duty_cycle = duty_cycle
        self.period_high = duty_cycle / freq
        self.period_low = (1 - duty_cycle) / freq
        logging.debug("Iniciando a thread ")

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.running = 1
        self.thread.start()

    def stop(self):
        self.running = 0

    def run(self):
        state = True
        self.gpio.high()
        start = timeit.default_timer()
        while self.running:
            passed_time = timeit.default_timer() - start
            if state:
                if passed_time >= self.period_high:
                    self.gpio.low()
                    state = False
                    start = timeit.default_timer()
            else:
                if passed_time >= self.period_low:
                    self.gpio.high()
                    state = True
                    start = timeit.default_timer()
