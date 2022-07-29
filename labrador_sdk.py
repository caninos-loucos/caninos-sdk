from typing import List
from dataclasses import dataclass, field

class CaninosSDK:
    INPUT = 0
    OUTPUT = 1
    OUTPUT = 2

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
    mode: any = CaninosSDK.OUTPUT
    alias: str = ""
    address: int = field(default=None, repr=False)

    def enable(self, mode, alias="", address=0x0):
        self.mode = mode
        self.alias = alias
        self.address = address
        self.board.register_enabled(self)

    def high(self):
        print(f"Setting pin {self.pin} to high.")


@dataclass
class Labrador():
    """Configuration for a Labrador board"""
    board_version: str = "64-v3.1"
    kernel_version: str = ">=4.19.98"
    enabled_features: list = field(default_factory=list)

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


if __name__ == '__main__':
    labrador = Labrador("64-v3.1", kernel_version=">=4.19.98")
    labrador.gpio3.enable(CaninosSDK.OUTPUT, alias="led_status")
    print(labrador, "\n")
    labrador.led_status.high()


"""python
# goal:

import CaninosSDK as k9

labrador = k9.Labrador("64-v3.1", kernel_version=">=4.19.98")

# configs
labrador.gpio0.enable(k9.OUTPUT, alias="led_status")
labrador.gpio.enable(2, k9.INPUT, alias="button1")
labrador.gpio.enable(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.gpio.enable(7, k9.I2C, address=0x4, alias="temp_sensor")

labrador.wifi.enable("CITI", "1cbe991a14")
labrador.camera.enable(k9.Webcam)

print(labrador.enabled_features())

# usage
labrador.led_status.high()
res = labrador.button1.read()
value = labrador.temp_sensor.read()

ip = labrador.wifi.get_ip()
ok, frame = labrador.camera.read()
"""
