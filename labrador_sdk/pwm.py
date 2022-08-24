import threading
import time

class PWM:
    freq = 0
    duty_cycle = 0
    period_high = 0
    period_low = 0
    thread:any
    gpio:any
    running: bool

    def __init__(self,gpio,freq,duty_cycle):
        self.gpio = gpio
        self.freq = freq
        self.duty_cycle = duty_cycle
        self.period_high = duty_cycle/freq
        self.period_low = (1-duty_cycle)/freq
        print("Iniciando a thread ")

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.running = 1
        self.thread.start()

    def stop(self):
        self.running = 0

    def run(self):
        while self.running:
            self.gpio.high()
            time.sleep(self.period_high)
            self.gpio.low()
            time.sleep(self.period_low)