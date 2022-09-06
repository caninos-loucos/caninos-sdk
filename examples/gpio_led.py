from labrador_sdk.gpio import GPIO
from labrador_sdk.main import Labrador
from labrador_sdk.pwm import PWM
import time


labrador = Labrador()
labrador.gpio15.enable_io(GPIO.Direction.OUTPUT, alias="led_status")
print(labrador, "\n")
for i in range(0, 6):
    labrador.led_status.high()
    time.sleep(0.5)
    labrador.led_status.low()
    time.sleep(0.5)
