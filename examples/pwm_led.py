from caninos_sdk.pin import Pin
from caninos_sdk.labrador import Labrador
from caninos_sdk.pwm import PWM
import time

labrador = Labrador()
labrador.pin13.enable_pwm(alias="led1", freq=50, duty_cycle=0.1)

labrador.led1.pwm.start()
time.sleep(3)
labrador.led1.pwm.stop()
