import caninos_sdk as k9
import time

labrador = k9.Labrador()
labrador.pin19.enable_gpio(k9.Pin.Direction.INPUT, alias="button1")
print(labrador, "\n")
while True:
    print(labrador.button1.read())
    time.sleep(0.1)
