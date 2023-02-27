import logging

logging.basicConfig(
    level="INFO",
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    datefmt="[%Y-%m-%d,%H:%M:%S]",
)

__version__ = "0.5.0"
SERIAL_USB = "/dev/ttyUSB0"
SERIAL_HEADER_40_PINS = "/dev/ttyS0"

from caninos_sdk.labrador import Labrador
from caninos_sdk.pin import Pin
from caninos_sdk.pwm import PWM
from caninos_sdk.camera import Camera
from caninos_sdk.serial import Serial
from caninos_sdk.i2c import I2C
