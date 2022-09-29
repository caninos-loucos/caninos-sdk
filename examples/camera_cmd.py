import caninos_sdk as k9
import typer, cv2, time


app = typer.Typer()
labrador = k9.Labrador()


@app.command()
def show(camera_id: int = 0):
    """
    Este comando mostra o que a câmera está vendo, a 10 frames por segundo.

    O id da câmera pode ser configurado com a opção --camera-id

    Exemplo:
        python examples/camera_cmd.py show --camera-id 0
    """
    ret = labrador.camera.enable(camera_id)
    if not ret:
        print("Erro ao habilitar a camera")

    while True:
        ok, frame = labrador.camera.read()
        if ok:
            print("Novo frame")
            cv2.imshow("labrador camera frame", frame)
            cv2.waitKey(1)
        else:
            print("A leitura veio vazia")
        time.sleep(0.1)


@app.command()
def save(filename: str = "frame.jpg", camera_id: int = 0):
    """
    Este comando lê uma imagem da câmera e salva em um arquivo.

    O nome do arquivo pode ser configurado com a opção --filename

    O id da câmera pode ser configurado com a opção --camera-id

    Exemplo:
        python examples/camera_cmd.py save --filename frame.jpg
    """
    ret = labrador.camera.enable(camera_id)
    if not ret:
        print("Erro ao habilitar a camera")

    ret = labrador.camera.save_frame(filename)
    if ret:
        print(f"O frame foi salvo no arquivo: {filename}")
    else:
        print("Houve um erro ao ler ou salvar o frame")

    labrador.camera.disable()


app()
