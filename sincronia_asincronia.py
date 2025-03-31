#CORRUTINAS

#Paso 1. Importar la asincronia
import asyncio

async def tareasAsincronas(numero,tarea):
    print(f"Iniciando la tareas numero: {numero}")
    await asyncio.sleep(2)#Simulacion par acompletar la tarea
    print(f"Se completo la tarea {numero} - {tarea}")

async def main():
    #simulacion para el ingreso de 10 tareas, 20 tareas, 50 tareas, 100tareas
    tareas=[tareasAsincronas(i,"PruebaTarea {i}") for i in range(100001)]
    await asyncio.gather(*tareas)


#Inicializar la simulacion asincrona
asyncio.run(main())