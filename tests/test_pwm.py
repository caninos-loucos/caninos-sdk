from labrador_sdk.gpio import GPIO
from labrador_sdk.pwm import PWM
from labrador_sdk.main import Labrador


def test_pwm():
    labrador = Labrador("64", kernel_version=">=4.19.98")
    labrador.gpio3.enable_pwm(alias="motor1", freq=1, duty_cycle=0.5)
    labrador.motor1.pwm.start()
    print("Oi\n")
