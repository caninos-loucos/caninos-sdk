from caninos_sdk.pin import Pin
from caninos_sdk.pwm import PWM
from caninos_sdk.labrador import Labrador


def test_pwm():
    labrador = Labrador("64", kernel_version=">=4.19.98")
