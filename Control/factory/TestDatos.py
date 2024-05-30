from SerialComunication import SerialComunication
import time
datos = SerialComunication("COM7")
print("conexion exitosa")
while True:
    time.sleep(.1)
    da= datos.getDatos()
    if(da != None):
        print(da)