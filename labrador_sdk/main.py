import time
from dataclasses import dataclass, field
from typing import List

from labrador_sdk.gpio import GPIO, gpio_mappings


@dataclass
class Labrador:
    """Configuration for a Labrador board"""

    board_version: str = "64"
    kernel_version: str = ">=4.19.98"
    enabled_features: list = field(default_factory=list)

    # FIXME: create an enum instead?
    VERSIONS = ["64", "32"]

    def __post_init__(self):
        if self.board_version not in Labrador.VERSIONS:
            raise f"Invalid board version {self.board_version}"
        self._load_gpios()

    def _load_gpios(self):
        for pin in gpio_mappings[self.board_version].keys():
            setattr(self, f"gpio{pin}", GPIO(pin, self))

    def register_enabled(self, periph):
        self.enabled_features.append(periph)
        setattr(self, f"{periph.alias}", periph)


if __name__ == "__main__":
    labrador = Labrador("64", kernel_version=">=4.19.98")
    labrador.gpio3.enable(GPIO.Direction.OUTPUT, alias="led_status")
    print(labrador, "\n")
    while True:
        labrador.led_status.high()
        time.sleep(0.5)
        labrador.led_status.low()
        time.sleep(0.5)
