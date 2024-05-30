import cv2

# Cargar el diccionario predefinido para los marcadores Aruco
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Crear el detector de Aruco con parámetros predeterminados
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

# Iniciar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("No se pudo abrir la cámara web.")

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (600, 600))

   
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected_candidates = detector.detectMarkers(gray)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame_resized, corners, ids)


    cv2.imshow("Detección de Aruco en tiempo real", frame_resized)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
