from dataclasses import dataclass, field

from gpiod import chip, line_request


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
    gpiod_pin: any = None

    def enable(self, mode, alias="", address=0x0):
        self.mode = mode
        self.alias = alias
        self.address = address
        self.board.register_enabled(self)
        self.gpiod_enable()

    def gpiod_enable(self):
        c = chip(f"/dev/gpiochip{4}")
        self.gpiod_pin = c.get_lines([3])
        config = line_request()
        config.consumer = "xxx label"
        config.request_type = line_request.DIRECTION_OUTPUT
        self.gpiod_pin.request(config)
        print(f"GPIO {self.pin} enabled")

    def high(self):
        # FIXME: actually make this toggle the pins
        print(f"Setting pin {self.pin} to high.")
        self.gpiod_pin.set_values([1])

    def low(self):
        print(f"Setting pin {self.pin} to low.")
        self.gpiod_pin.set_values([0])

