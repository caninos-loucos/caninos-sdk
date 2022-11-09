import caninos_sdk as k9
import time

# XXX: module under development

labrador = k9.Labrador()
labrador.serial.enable(port="/dev/ttyS0", baudrate=9600, alias="arduino_uart")

labrador.serial_usb.enable(baudrate=9600, alias="arduino_uart") # default port /dev/ttyUSB0, overridable
# labrador.serial_header.enable(baudrate=9600, alias="arduino_uart") # default port /dev/ttyS0
# labrador.serial.enable(port="/dev/ttyS0", baudrate=9600, alias="arduino_uart") # default port /dev/ttyS0

labrador.arduino_uart.write(b"dados importantes")
respostas = labrador.arduino_uart.read()
