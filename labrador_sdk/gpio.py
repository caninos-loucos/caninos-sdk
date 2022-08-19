import logging
import platform
from dataclasses import dataclass, field

from gpiod import chip, line_request


class IO:
    # FIXME: use proper enums
    INPUT = 0
    OUTPUT = 1
    I2C = 2
    PWM = 3
    SPI = 4


# FIXME: add this to a class
gpio_mappings = {}
gpio_mappings["64"] = {
    36: "A28",
    33: "B0",
    35: "B1",
    37: "B2",
    12: "B8",
    31: "B10",
    32: "B13",
    28: "B14",
    29: "B15",
    27: "B16",
    7: "B18",
    26: "B19",
    11: "C0",
    13: "C1",
    15: "C4",
    22: "C5",
    18: "C6",
    24: "C23",
    21: "C24",
    16: "D30",
    3: "E3",
    5: "E2",
}
gpio_mappings["32"] = {
    36: "A28",
    33: "B0",
    35: "B1",
    37: "B2",
    12: "B8",
    31: "B10",
    32: "B13",
    28: "B14",
    29: "B15",
    27: "B16",
    7: "B18",
    26: "B19",
    11: "C0",
    13: "C1",
    15: "C4",
    22: "C5",
    18: "C6",
    24: "C23",
    21: "C24",
    16: "D30",
    3: "E3",
    5: "E2",
}

# FIXME: implement this
# gpio_mappings["Virtual"] = {36: "A28", 33: "B0", 35: "B1", 37: "B2", 12: "B8", 31: "B10", 32: "B13", 28: "B14", 29: "B15", 27: "B16", 7:  "B18", 26: "B19", 11: "C0", 13: "C1", 15: "C4", 22: "C5", 18: "C6", 24: "C23", 21: "C24", 16: "D30", 3:  "E3", 5:  "E2"}


@dataclass
class GPIO:
    pin: int
    board: any = field(repr=False)
    chip_id: str = field(default=None, repr=False)
    line_id: int = field(default=None, repr=False)
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
        if platform.machine() == "x86_64":
            logging.debug("Will not enable GPIO in PC.")
            return
        c = chip(f"/dev/gpiochip{4}")
        self.gpiod_pin = c.get_lines([3])
        config = line_request()
        config.consumer = "xxx label"
        config.request_type = line_request.DIRECTION_OUTPUT
        self.gpiod_pin.request(config)
        print(f"GPIO {self.pin} enabled")

    def high(self):
        if platform.machine() == "x86_64":
            logging.debug("Will not enable GPIO in PC.")
            return
        # FIXME: actually make this toggle the pins
        print(f"Setting pin {self.pin} to high.")
        self.gpiod_pin.set_values([1])

    def low(self):
        if platform.machine() == "x86_64":
            logging.debug("Will not enable GPIO in PC.")
            return
        print(f"Setting pin {self.pin} to low.")
        self.gpiod_pin.set_values([0])

    def get_offset_32bits(group):
        group_ascii = ord(group)
        assert group_ascii in range(ord("A"), ord("E") + 1)
        return 32 * (group_ascii - ord("A"))

    def get_num(pin, board_bits):
        group = dict.get(gpio_mappings[board_bits], pin)
        if not group:
            logging.error(f"Invalid pin {pin}")
            return
        if board_bits == "32":
            offset = GPIO.get_offset_32bits(group[0])
            group_n = int(group[1:])
            return 0, offset + group_n
        elif board_bits == "64":
            chip_id = ord(group[0]) - ord("A")
            line_id = int(group[1])
            return chip_id, line_id
