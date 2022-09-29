from dataclasses import dataclass, field
from typing import List
from caninos_sdk.pin import Pin, gpio_mappings
from caninos_sdk.pwm import PWM
from caninos_sdk.camera import Camera
import logging, platform, time


@dataclass
class Labrador:
    """Configuration for a Labrador board"""

    board_version: str = "64"
    cpu_architecture: str = "aarch64"
    kernel_version: str = "4.19.98"
    enabled_features: list = field(default_factory=list)

    # FIXME: create an enum instead?
    VERSIONS = ["64", "32"]

    def __post_init__(self):
        self.cpu_architecture = platform.machine()
        self.board_version = platform.architecture()[0][:2]
        self.kernel_version = platform.release()
        self.camera = Camera(self)
        self._load_pins()

    def _load_pins(self):
        for pin in gpio_mappings[self.board_version].keys():
            setattr(self, f"pin{pin}", Pin(pin, self))

    def register_enabled(self, periph):
        self.enabled_features.append(periph)
        if hasattr(periph, "alias"):
            setattr(self, f"{periph.alias}", periph)
