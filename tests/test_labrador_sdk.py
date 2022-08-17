def test_import_from():
    from labrador_sdk import __version__, main
    from labrador_sdk.main import Labrador

    assert __version__ == "0.1.0"
    print(main)
    print(main.Labrador)


def test_import_as():
    import labrador_sdk as k9

    assert k9.__version__ == "0.1.0"
    print(k9.main)
    print(k9.main.Labrador)
