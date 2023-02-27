# Caninos SDK

Estamos criando uma SDK para fazer com que o uso da Labrador fique **muito acessível**.
O objetivo é permitir códigos assim:

```python
# as linhas abaixo já funcionam:
import caninos_sdk as k9
labrador = k9.Labrador()
labrador.pin15.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")
labrador.pin19.enable_gpio(k9.Pin.Direction.INPUT, alias="button1")
labrador.i2c.add_device("arduino_i2c", 4)
labrador.camera.enable()

# as próximas ainda não (precisa ser desenvolvido)
labrador.pin.enable_gpio(k9.cpu_pin(0x33), k9.INPUT, alias="button1")
labrador.pin.enable_gpio(9, k9.SPI, address=0x4, alias="temp_sensor2")
labrador.wifi.enable("CITI", "1cbe991a14")

print(labrador.enabled_features())

# uso
labrador.led_status.high() # já funciona
res = labrador.button1.read() # já funciona
res = labrador.arduino_i2c.read(2) # já funciona
value = labrador.temp_sensor1.read() # ainda não

ip = labrador.wifi.get_ip() # ainda não
ok, frame = labrador.camera.read() # já funciona
```

Caso queira ajudar com a implementação, dê uma olhadinha nos [issues](https://github.com/caninos-loucos/caninos-sdk/issues).

# Instalação

Instale a Caninos SDK com o seguinte comando:
- `pip3 install caninos-sdk`

⚠️ Caso apareça o erro "pip not installed", isso quer dizer que sua Labrador ainda não tem o comando `pip3`. Instale-o com o comando a seguir, e depois tente de novo.
- `sudo apt install python3-dev python3-pip python3-setuptools `

Por fim, configure as permissões do GPIO, I2C e Serial, para que não precise usar `sudo`:

```bash
sudo chmod +x ./setup-periph-permissions.sh
sudo ./setup-periph-permissions.sh
```

# Exemplo

Para testar a SDK vamos piscar um LED -- o _hello world_ do hardware :)

Abra um terminal, digite `python3`, e vá inserindo os comandos abaixo, um de cada vez:

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
```

## Outros exemplos

Confira a pasta [examples](https://github.com/caninos-loucos/caninos-sdk/tree/main/examples) do repositório no GitHub.

### Câmera
Para usar a câmera, é necessário instalar o [OpenCV](https://linuxize.com/post/how-to-install-opencv-on-debian-10/). Instale-o com o comando abaixo:
```bash
sudo apt install python3-opencv
```

### I2C
Para usar o I2C, é necessário instalar a [pylibi2c](https://github.com/amaork/libi2c). Instale-a com os comandos abaixo:
```bash
git clone https://github.com/amaork/libi2c.git
cd libi2c && pip3 install .
```

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

Update the version number at `__init__.py`.

```bash
# build the new version
python3 -m build

# deploy
VERSION=$(grep -r "__version__" caninos_sdk/__init__.py | sed -E 's/.* = "(.*)"/\1/g')
twine upload dist/caninos_sdk-$VERSION-py3-none-any.whl  --config-file ${HOME}/.pypirc
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
- [x] support i2c
- [x] support serial
- [x] support camera
- [ ] support spi
- [ ] support wifi
- [ ] support bluetooth

Other notes:
- should this library support other SBCs?
- should the docs be in English or Portuguese?
- get funding or community help
