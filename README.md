# Caninos SDK

Estamos criando uma SDK para fazer com que o uso da Labrador fique **muito acessível**.
O objetivo é permitir códigos assim:

```python
# as 4 linhas abaixo já funcionam:
import caninos_sdk as k9
labrador = k9.Labrador()
labrador.pin15.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")
labrador.camera.enable()

# as próximas 5 ainda não (precisa ser desenvolvido)
labrador.pin12.enable_gpio(k9.Pin.Direction.INPUT, alias="button1")
labrador.pin.enable_gpio(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.pin.enable_gpio(7, k9.I2C, address=0x4, alias="temp_sensor")
labrador.pin.enable_gpio(9, k9.SPI, address=0x4, alias="temp_sensor")
labrador.wifi.enable("CITI", "1cbe991a14")

print(labrador.enabled_features())

# uso
labrador.led_status.high() # já funciona
res = labrador.button1.read() # ainda não
value = labrador.temp_sensor.read() # ainda não

ip = labrador.wifi.get_ip() # ainda não
ok, frame = labrador.camera.read() # já funciona
```

Caso queira ajudar com a implementação, dê uma olhadinha nos [issues](https://github.com/caninos-loucos/caninos-sdk/issues).

# Começando

## Piscando um LED - o Hello World do hardware

```python
# importa a SDK e dá a ela um apelido bonitinho
import caninos_sdk as k9

# instancia o objeto labrador
labrador = k9.Labrador()

# habilita o pino 15 como saída, e dá a ele o apelido "led_status"
labrador.pin15.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")

# liga o "led_status"
labrador.led_status.high()
# desliga o "led_status"
labrador.led_status.low()
# liga o mesmo led de novo, porém agora se referindo a ele pelo número do pino
labrador.pin15.high()
```

**⚠️ Atenção**: para usar as GPIOs sem `sudo`, é necessário rodar os comandos abaixo, toda vez que se reinicia a placa:

```bash
sudo chown caninos /dev/gpiochip*
sudo chmod g+rw /dev/gpiochip*
```

## Outros exemplos

Confira a pasta [examples](https://github.com/caninos-loucos/caninos-sdk/tree/main/examples) do repositório no GitHub.

**⚠️ Atenção**: para usar a câmera, é necessário instalar o [OpenCV](https://linuxize.com/post/how-to-install-opencv-on-debian-10/). Instale-o com o comando abaixo:
- `sudo apt install python3-opencv`

# Contributing

First, see the [issues](https://github.com/caninos-loucos/caninos-sdk/issues) page.

Then, install some dependencies:

```bash
sudo apt install python3-dev python3-pip python3-setuptools libffi-dev libssl-dev curl
pip3 install --upgrade pip
```

Finally, install the package locally in _editable_ form:
```bash
pip3 install -e .
```


## Publish a new version
Install build deps: `pip3 install build twine`.

Update the version number at `__init__.py` and `setup.cfg`.

```bash
# build the new version
python3 -m build

# deploy
twine upload -r testpypi dist/*.whl # to https://test.pypi.org/
twine upload -r dist/*.whl # to https://pypi.org/
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
