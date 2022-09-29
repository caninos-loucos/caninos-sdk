# caninos-sdk

A ideia é fazer com que o uso dos periféricos da Labrador seja **muito acessível**, ao ponto de, um dia, permitir códigos assim:

```python
import caninos_sdk as k9

# as 4 linhas abaixo já funcionam:
labrador = k9.Labrador()
labrador.pin15.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")
labrador.pin2.enable_gpio(k9.Pin.Direction.INPUT, alias="button1")
labrador.camera.enable()

# as próximas 3 ainda não
labrador.pin.enable_gpio(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.pin.enable_gpio(7, k9.I2C, address=0x4, alias="temp_sensor")
labrador.wifi.enable("CITI", "1cbe991a14")

print(labrador.enabled_features())

# uso
labrador.led_status.high() # já funciona
res = labrador.button1.read() # ainda não
value = labrador.temp_sensor.read() # ainda não

ip = labrador.wifi.get_ip() # ainda não
ok, frame = labrador.camera.read() # já funciona
```

# Começando

Pode testar rodando um dos exemplos. Se for usar o gpio: `python3 examples/gpio_led.py`.

Note que, para habilitar o uso das GPIOs sem `sudo`, precisa rodar esses comandos (por enquanto) toda vez que reinicia a placa:

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
- [x] make the gpios actually work (read/write)
~~- [ ] create default constructors/subclasses for specific boards~~
~~- [ ] create a "VirtualLabrador" class, for tests and remote labs~~
- [x] refactor to a proper python package using modern python conventions
- [-] write unit tests -> works with `pytest -s`
- [x] gpio read/write work across Labradors 32/64
- [x] support pwm
- [ ] support i2c
- [ ] support spi
- [ ] support wifi
- [x] support camera

Other notes:
- should this library support other SBCs?
- should the docs be in English or Portuguese?
- need to get funding or community help
