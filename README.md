# labrador-sdk

The goal is to enable something like this:
```python
import CaninosSDK as k9

labrador = k9.Labrador("64-v3.1", kernel_version=">=4.19.98")

# configs
labrador.gpio0.enable(k9.OUTPUT, alias="led_status")
labrador.gpio2.enable(k9.INPUT, alias="button1")
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

# TO-DO:
- [x] initial sketch to prove the concept
- [ ] make the gpios actually work (read/write)
- [ ] create default constructors/subclasses for specific boards
- [ ] create a "VirtualLabrador" class, for tests and remote labs
- [-] refactor to a proper python package
- [ ] write unit tests
- [ ] gpio read/write work across Labradors 32/64
- [ ] support pwm
- [ ] support i2c
- [ ] support spi
- [ ] support wifi
- [ ] support camera

Other notes:
- should this library support other SBCs?
- should the docs be in English or Portuguese?
- need to get funding or community help

# Setup

Para habilitar o uso das GPIOs sem sudo, rode esses comandos:

```bash
sudo chown caninos /dev/gpiochip*
sudo chmod g+rw /dev/gpiochip*
```

# Development -- if you are helping build this lib

```bash
pip3 install poetry
```

