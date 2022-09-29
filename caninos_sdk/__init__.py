import logging

logging.basicConfig(
    level="INFO",
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    datefmt="[%Y-%m-%d,%H:%M:%S]",
)

__version__ = "0.2.3"

from caninos_sdk.labrador import Labrador
from caninos_sdk.pin import Pin
from caninos_sdk.pwm import PWM
from caninos_sdk.camera import Camera
