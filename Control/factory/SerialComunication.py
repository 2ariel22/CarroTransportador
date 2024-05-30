import serial
import time

class SerialComunication():
    def __init__(self, COM):
        self.conexion = serial.Serial(COM)
        self.conexion.timeout = 1  # Timeout de 1 segundo para la lectura

    def getDatos(self):
        rawString = self.conexion.readline().decode().strip()
        if rawString:
            data = tuple(rawString.split(":"))
            return data[1]
        else:
            return None
        
    def sendDatos(self, data: str):
        self.conexion.write(data.encode())
        # Esperar confirmación de recepción
        while True:
            if self.conexion.in_waiting > 0:
                confirmation = self.conexion.readline().decode().strip()
                if confirmation == "RECIBIDO":
                    break

    def closeConexion(self):
        self.conexion.close()
