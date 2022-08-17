from dataclasses import dataclass, field
from typing import List


class IO:
    # FIXME: use proper enums
    INPUT = 0
    OUTPUT = 1
    I2C = 2


# FIXME: add this to a class
gpio_mappings = {}
gpio_mappings["64-v3.1"] = {
    3: "E3",
    5: "E2",
    7: "B18",
}


@dataclass
class GPIO:
    pin: int
    board: any = field(repr=False)
    group: str = field(default=None, repr=False)
    offset: int = field(default=None, repr=False)
    mode: any = IO.OUTPUT
    alias: str = ""
    address: int = field(default=None, repr=False)

    def enable(self, mode, alias="", address=0x0):
        self.mode = mode
        self.alias = alias
        self.address = address
        self.board.register_enabled(self)
        # FIXME: actually make this enable the pin

    def high(self):
        # FIXME: actually make this toggle the pins
        print(f"Setting pin {self.pin} to high.")


@dataclass
class Labrador:
    """Configuration for a Labrador board"""

    board_version: str = "64-v3.1"
    kernel_version: str = ">=4.19.98"
    enabled_features: list = field(default_factory=list)

    # FIXME: create an enum instead?
    VERSIONS = ["64-v3.1", "32-v2.0"]

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
    labrador = Labrador("64-v3.1", kernel_version=">=4.19.98")
    labrador.gpio3.enable(IO.OUTPUT, alias="led_status")
    print(labrador, "\n")
    labrador.led_status.high()
