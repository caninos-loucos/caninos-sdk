import caninos_sdk as k9

labrador = k9.Labrador()
labrador.serial_usb.enable("arduino_serial", baudrate=9600, timeout=3)

labrador.arduino_serial.write(b'dados enviados via serial')
ret = labrador.arduino_serial.read(10)
print("Lido da serial:", ret)

labrador.arduino_serial.close()
