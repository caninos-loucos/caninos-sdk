from dataclasses import dataclass
import logging, glob

# requer esta biblioteca, mas ela não está no pip: https://github.com/amaork/libi2c

@dataclass
class I2C:
    """
    Provides access to the Labrador's default I2C bus.

    - Pin 3: SDA (data)
    - Pin 5: SCK (clock)
    """

    alias: str
    address: int
    libi2c_device = None
    linux_port = "/dev/i2c-2"

    def __post_init__(self):
        import pylibi2c
        self.libi2c_device = pylibi2c.I2CDevice(self.linux_port, self.address)

    def write(self, data):
        return self.libi2c_device.write(0x0, data)

    def read(self, amount_bytes):
        return self.libi2c_device.read(0x0, amount_bytes)

class I2CFactory:
    def __init__(self, board):
        self.board = board

    def add_device(self, alias, address):
        """
        Enables a new I2C device at a specific address.
        """
        i2c_periph = I2C(alias, address)
        self.board.register_enabled(i2c_periph)

    def list_ports(self):
        return glob.glob("/dev/i2c*")
