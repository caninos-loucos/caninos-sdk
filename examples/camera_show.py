from caninos_sdk.labrador import Labrador
import sys, time, cv2

labrador = Labrador()

camera_id = int(sys.argv[1]) if len(sys.argv) == 2 else 0
if not labrador.camera.enable(camera_id):
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
