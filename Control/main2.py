import asyncio
from factory.SerialComunication import SerialComunication

import cv2
from concurrent.futures import ThreadPoolExecutor

async def avanzar(comunication, duration):
    print("Avanzando")
    datos_avanzar = "1,0,255,1,0,245"  # Ajusta estos valores según tu lógica de movimiento
    comunication.sendDatos(datos_avanzar)
    await asyncio.sleep(duration)

async def retroceder(comunication, duration):
    print("Retrocediendo")
    datos_retroceder = "0,1,255,0,1,255"  # Ajusta estos valores según tu lógica de retroceso
    comunication.sendDatos(datos_retroceder)
    await asyncio.sleep(duration)

async def girar_derecha(comunication, duration):
    print("Girando a la derecha")
    datos_girar_derecha = "1,0,255,0,1,255"  # Ajusta estos valores según tu lógica de giro a la derecha
    comunication.sendDatos(datos_girar_derecha)
    await asyncio.sleep(duration)

async def girar_izquierda(comunication, duration):
    print("Girando a la izquierda")
    datos_girar_izquierda = "0,1,255,1,0,255"  # Ajusta estos valores según tu lógica de giro a la izquierda
    comunication.sendDatos(datos_girar_izquierda)
    await asyncio.sleep(duration)

async def detener(comunication, duration):
    print("Deteniendo")
    datos_detener = "0,0,0,0,0,0"
    comunication.sendDatos(datos_detener)
    await asyncio.sleep(duration)

# Rutina 1: Avanzar, girar derecha, retroceder
async def rutina_1():
    comunication = SerialComunication("COM3")
    print("Comunicación exitosa")
    try:
        await avanzar(comunication, 10)
        await detener(comunication, 0.5)
        await girar_derecha(comunication, .3)
        await detener(comunication, 0.5)
        await retroceder(comunication, 10)
        await detener(comunication, 0.5)
    finally:
        comunication.closeConexion()
        print("Conexión cerrada")

# Rutina 2: Avanzar, girar izquierda, retroceder
async def rutina_2():
    comunication = SerialComunication("COM3")
    print("Comunicación exitosa")
    try:
        await avanzar(comunication, 10)
        await detener(comunication, 0.5)
        await girar_izquierda(comunication, .3)
        await detener(comunication, 0.5)
        await retroceder(comunication, 10)
        await detener(comunication, 0.5)
    finally:
        comunication.closeConexion()
        print("Conexión cerrada")

# Rutina 3: Girar derecha, avanzar, girar izquierda
async def rutina_3():
    comunication = SerialComunication("COM3")
    print("Comunicación exitosa")
    try:
        await avanzar(comunication, 20)
        await detener(comunication, 0.5)
    finally:
        comunication.closeConexion()
        print("Conexión cerrada")

# Función para iniciar la rutina correspondiente
def iniciar_rutina(rutina):
    if rutina == 1:
        asyncio.run(rutina_1())
    elif rutina == 24:
        asyncio.run(rutina_2())
    elif rutina == 50:
        asyncio.run(rutina_3())

# Cargar el diccionario predefinido para los marcadores Aruco
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Crear el detector de Aruco con parámetros predeterminados
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

# Iniciar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("No se pudo abrir la cámara web.")

# Usamos un ThreadPoolExecutor para ejecutar las rutinas en hilos separados
executor = ThreadPoolExecutor(max_workers=3)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (600, 600))
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected_candidates = detector.detectMarkers(gray)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame_resized, corners, ids)
        # Iniciar la rutina correspondiente al ID detectado
        if 1 in ids:
            print("ID 1 detectado. Iniciando rutina 1...")
            executor.submit(iniciar_rutina, 1)
        elif 24 in ids:
            print("ID 24 detectado. Iniciando rutina 2...")
            executor.submit(iniciar_rutina, 24)
        elif 50 in ids:
            print("ID 50 detectado. Iniciando rutina 3...")
            executor.submit(iniciar_rutina, 50)

    cv2.imshow("Detección de Aruco en tiempo real", frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
