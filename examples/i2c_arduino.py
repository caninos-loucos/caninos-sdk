import caninos_sdk as k9

labrador = k9.Labrador()
labrador.i2c.enable(port="/dev/i2c-2", address=0x4, alias="arduino_i2c")

labrador.arduino_i2c.write(b"dados importantes")
respostas = labrador.arduino_i2c.read()
