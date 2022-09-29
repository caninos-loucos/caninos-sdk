from caninos_sdk.pin import Pin
from caninos_sdk.pwm import PWM
from caninos_sdk.labrador import Labrador


def test_pwm():
    labrador = Labrador("64", kernel_version=">=4.19.98")
    labrador.pin3.enable_pwm(alias="motor1", freq=1, duty_cycle=0.5)
    print("Oi\n")
