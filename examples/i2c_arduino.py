import caninos_sdk as k9

labrador = k9.Labrador()
labrador.i2c.add_device("arduino_i2c", 4)

ret = labrador.arduino_i2c.write(b"dados importantes")
print(ret)
ret = labrador.arduino_i2c.read(2)
print(ret)
