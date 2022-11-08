from dataclasses import dataclass, field
import logging, glob

# requer esta biblioteca, mas ela não está no pip: https://github.com/amaork/libi2c

@dataclass
class I2C:
    """
    Provides access to the Labrador's default I2C bus.

    - Pin 3: SDA (data)
    - Pin 5: SCK (clock)
    """

    board: any
    address: int = None
    alias: str = ""
    linux_port = "/dev/i2c-2"
    libi2c_device = None

    def __post_init__(self):
        # FIXME
        import pylibi2c
        self.pylibi2c = pylibi2c

    def enable(self, address, alias=""):
        """
        Enables a new I2C device at a specific address.
        """
        self.address = address
        self.alias = alias
        self.libi2c_device = self.pylibi2c.I2CDevice(self.linux_port, address)
        self.board.register_enabled(self)

    def write(self, data):
        return self.libi2c_device.write(0x0, data)

    def read(self, amount_bytes):
        return self.libi2c_device.read(0x0, amount_bytes)

    def list_ports(self):
        return glob.glob("/dev/i2c*")
