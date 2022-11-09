"""
Para usar esse exemplo, grave o código abaixo em um arduino e conecte
os pinos conforme a lista abaixo:

Arduino Uno | Labrador
    GND     |  Pino 6 (ou qualquer outro GND)
    SDA     |  Pino 3
    SCL     |  Pino 5

#include <Wire.h>
void setup()
{
  Wire.begin(4); // o endereço do device i2c será 4 (0x04)
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}
void loop() { delay(100); }
void receiveEvent(int howMany)
{
  while(Wire.available() > 0) {
    char c = Wire.read();
    Serial.print(c); // imprimir o que foi recebido na serial
  }
}
"""

import caninos_sdk as k9

labrador = k9.Labrador()
labrador.i2c.add_device("arduino_i2c", 4)

ret = labrador.arduino_i2c.write(b"dados importantes\n")
print(ret)
ret = labrador.arduino_i2c.read(2)
print(ret)
