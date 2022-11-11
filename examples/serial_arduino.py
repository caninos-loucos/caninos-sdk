import sys
import caninos_sdk as k9

labrador = k9.Labrador()

if len(sys.argv) == 2 and sys.argv[1] == "--header":
    labrador.serial_header40pins.enable("arduino_serial", baudrate=9600, timeout=3)
else:
    labrador.serial_usb.enable("arduino_serial", baudrate=9600, timeout=3)

labrador.arduino_serial.write(b'dados enviados via serial')
ret = labrador.arduino_serial.read(10)
print("Lido da serial:", ret)

labrador.arduino_serial.close()
