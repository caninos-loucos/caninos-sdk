def test_import_from():
    from caninos_sdk import __version__, labrador
    from caninos_sdk.labrador import Labrador

    print(labrador)
    print(labrador.Labrador)


def test_import_as():
    import caninos_sdk as k9

    print(k9.labrador)
    print(k9.labrador.Labrador)
