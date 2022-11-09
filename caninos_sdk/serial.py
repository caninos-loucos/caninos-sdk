from dataclasses import dataclass
import caninos_sdk
import glob, serial


@dataclass
class Serial:
    board: any
    default_port: str
    alias: str = ""

    def enable(self, alias, **kwargs):
        self.alias = alias
        self.pyserial_handle = serial.Serial(caninos_sdk.SERIAL_USB, **kwargs)
        self.board.register_enabled(self)

    def disable(self):
        self.pyserial_handle.close()
        self.alias = ""
        self.board.register_disabled(self)

    def __getattr__(self, attr):
        """
        Fallback for not implemented methods: if pyserial has that method, then return it.
        """
        if hasattr(self.pyserial_handle, attr):
            return getattr(self.pyserial_handle, attr)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

    def list_ports(self):
        return glob.glob("/dev/ttyS*") + glob.glob("/dev/ttyUSB*")
