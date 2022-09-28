import caninos_sdk as k9
import time


labrador = k9.Labrador()
labrador.pin15.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")
print(labrador, "\n")
for i in range(0, 6):
    labrador.led_status.high()
    time.sleep(0.5)
    labrador.led_status.low()
    time.sleep(0.5)
