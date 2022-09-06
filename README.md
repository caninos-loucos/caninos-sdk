# caninos-sdk

A ideia é fazer com que o uso dos periféricos da Labrador seja **muito acessível**, ao ponto de, um dia, permitir códigos assim:

```python
import CaninosSDK as k9

labrador = k9.Labrador("64-v3.1", kernel_version=">=4.19.98")

# configurações
labrador.gpio1.enable(k9.OUTPUT, alias="led_status")
labrador.gpio2.enable(k9.INPUT, alias="button1")
labrador.gpio.enable(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.gpio.enable(7, k9.I2C, address=0x4, alias="temp_sensor")

labrador.wifi.enable("CITI", "1cbe991a14")
labrador.camera.enable(k9.Webcam)

print(labrador.enabled_features())

# uso
labrador.led_status.high()
res = labrador.button1.read()
value = labrador.temp_sensor.read()

ip = labrador.wifi.get_ip()
ok, frame = labrador.camera.read()
```

# Começando

Por enquanto, pode testar rodando `python3 labrador_sdk/main.py`.

Note que, para habilitar o uso das GPIOs sem `sudo`, rode esses comandos (por enquanto precisa rodar toda vez que reinicia a placa):

```bash
sudo chown caninos /dev/gpiochip*
sudo chmod g+rw /dev/gpiochip*
```


# Contributing

See: https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/

Install dependencies:
```bash
sudo apt install python3-dev python3-pip python3-setuptools libffi-dev libssl-dev curl
pip3 install --upgrade pip
```

To install the package locally in _editable_ form:
```bash
pip3 install -e .
```

## Publish a new version
Install build deps: `pip3 install build twine`.

```bash
twine upload -r testpypi dist/* # deploy to https://test.pypi.org/
twine upload -r dist/* # deploy to https://pypi.org/
```


## TO-DO:
- [x] initial sketch to prove the concept
- [-] make the gpios actually work (read/write)
- [ ] create default constructors/subclasses for specific boards
- [ ] create a "VirtualLabrador" class, for tests and remote labs
- [x] refactor to a proper python package using modern python conventions
- [-] write unit tests -> works with `pytest -s`
- [-] gpio read/write work across Labradors 32/64
- [ ] support pwm
- [ ] support i2c
- [ ] support spi
- [ ] support wifi
- [ ] support camera

Other notes:
- should this library support other SBCs?
- should the docs be in English or Portuguese?
- need to get funding or community help
