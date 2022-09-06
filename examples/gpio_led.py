import time

from labrador_sdk.gpio import GPIO
from labrador_sdk.main import Labrador
from labrador_sdk.pwm import PWM

labrador = Labrador()
labrador.gpio3.enable_io(GPIO.Direction.OUTPUT, alias="led_status")
print(labrador, "\n")
while True:
    labrador.led_status.high()
    time.sleep(0.5)
    labrador.led_status.low()
    time.sleep(0.5)
