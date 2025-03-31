#Paso 1. importar las librerias
import asyncio
import random

#Paso 2. Crear las funciones para obtgner los datos
async def obtnerDatos(peticion):
    print(f"Solicitando datos al servidor {peticion}")
    tiempoEspera=random.uniform(1,3)
    #Simulacion del tiempo entre 1 a 3 segundos
    await asyncio.sleep(tiempoEspera)
    print(f"Datos obtenidos correctamente en un tiempo de  {tiempoEspera}")
    return f"Datos {peticion}"

async def main():
    peticiones=[obtnerDatos(i) for i in range(10000)]
    resultados= await asyncio.gather(*peticiones)
    print("Solicitudes completadas")
    for resultado in resultados:
        print(resultado) 

asyncio.run(main())