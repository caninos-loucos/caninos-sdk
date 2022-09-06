import imp
import logging
import platform
import time
from dataclasses import dataclass, field
from typing import List

from labrador_sdk.gpio import GPIO, gpio_mappings
from labrador_sdk.pwm import PWM


@dataclass
class Labrador:
    """Configuration for a Labrador board"""

    board_version: str = "64"
    cpu_architecture: str = "aarch64"
    kernel_version: str = "4.19.98"
    # desired_kernel_version: str = ">=4.19.98"
    enabled_features: list = field(default_factory=list)

    # FIXME: create an enum instead?
    VERSIONS = ["64", "32"]

    def __post_init__(self):
        self.cpu_architecture = platform.machine()
        self.board_version = platform.architecture()[0][:2]
        self.kernel_version = platform.release()
        self._load_gpios()

    def _load_gpios(self):
        for pin in gpio_mappings[self.board_version].keys():
            setattr(self, f"gpio{pin}", GPIO(pin, self))

    def register_enabled(self, periph):
        self.enabled_features.append(periph)
        setattr(self, f"{periph.alias}", periph)
