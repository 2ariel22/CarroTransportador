import asyncio
from factory.SerialComunication import SerialComunication

async def avanzar(comunication, duration):
    print("Avanzando")
    datos_avanzar = "1,0,255,1,0,255"  # Ajusta estos valores según tu lógica de movimiento
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

async def main():
    # Configura la comunicación serie
    comunication = SerialComunication("COM3")
    print("Comunicación exitosa")

    # Rutina del robot usando las funciones definidas
    try:
        # Avanzar 1 segundo
        await avanzar(comunication, 5)

        # Detener 0.5 segundos
        await detener(comunication, .4)

        # Girar a la derecha 1 segundo
        await girar_derecha(comunication, .3)

        # Detener 0.5 segundos
        await detener(comunication, 0.4)

        # Retroceder 1 segundo
        await retroceder(comunication, 5)

        # Detener 0.5 segundos
        await detener(comunication, 0.4)

    finally:
        # Cierra la conexión serie
        comunication.closeConexion()
        print("Conexión cerrada")

# Ejecutar la rutina asíncrona
asyncio.run(main())
