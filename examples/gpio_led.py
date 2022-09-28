from caninos_sdk.pin import Pin
from caninos_sdk.labrador import Labrador
import time


labrador = Labrador()
labrador.pin15.enable_gpio(Pin.Direction.OUTPUT, alias="led_status")
print(labrador, "\n")
for i in range(0, 6):
    labrador.led_status.high()
    time.sleep(0.5)
    labrador.led_status.low()
    time.sleep(0.5)
