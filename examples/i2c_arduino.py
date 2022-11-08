import caninos_sdk as k9

labrador = k9.Labrador()
labrador.i2c.enable(4, alias="arduino_i2c")

ret = labrador.arduino_i2c.write(b"dados importantes")
print(ret)
ret = labrador.arduino_i2c.read(2)
print(ret)
