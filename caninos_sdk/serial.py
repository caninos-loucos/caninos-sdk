from dataclasses import dataclass, field
from caninos_sdk.pwm import PWM
import logging, platform, serial, glob

# XXX: module under development


@dataclass
class Serial:
    port: str

    def __post_init__(self):
        pass

    def enable(self, direction, alias=""):
        pass
        # serial.open ...

    def list_ports(self):
        return glob.glob("/dev/ttyS*") + glob.glob("/dev/ttyUSB*")
