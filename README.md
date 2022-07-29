# labrador-sdk

Goal:
```python

import CaninosSDK as k9

labrador = k9.Labrador("64-v3.1", kernel_version=">=4.19.98")

# configs
labrador.gpio0.enable(k9.OUTPUT, alias="led_status")
labrador.gpio.enable(2, k9.INPUT, alias="button1")
labrador.gpio.enable(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.gpio.enable(7, k9.I2C, address=0x4, alias="temp_sensor")

labrador.wifi.enable("CITI", "1cbe991a14")
labrador.camera.enable(k9.Webcam)

print(labrador.enabled_features())

# usage
labrador.led_status.high()
res = labrador.button1.read()
value = labrador.temp_sensor.read()

ip = labrador.wifi.get_ip()
ok, frame = labrador.camera.read()
```
