from caninos_sdk.pin import Pin


def test_gpio_pin_32bits():
    chip, line = Pin.get_num(3, "32")  # GPIOE3
    assert chip == 0
    assert line == 131


def test_gpio_pin_64bits():
    chip, line = Pin.get_num(3, "64")  # GPIOE3
    assert chip == 4
    assert line == 3
