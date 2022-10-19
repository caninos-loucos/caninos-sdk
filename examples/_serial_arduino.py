import caninos_sdk as k9
import time

# XXX: module under development

labrador = k9.Labrador()
labrador.serial.enable(port="/dev/ttyS0", baudrate=9600, alias="arduino_uart")

labrador.arduino_uart.write(b"dados importantes")
respostas = labrador.arduino_uart.read()
