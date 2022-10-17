from dataclasses import dataclass, field
from caninos_sdk.pwm import PWM
import logging, platform, glob

# instalar essa biblioteca: https://github.com/amaork/libi2c


@dataclass
class I2C:
    port: str

    def __post_init__(self):
        pass

    def enable(self, direction, alias=""):
        pass
        # serial.open ...

    def list_ports(self):
        return glob.glob("/dev/i2c*")
