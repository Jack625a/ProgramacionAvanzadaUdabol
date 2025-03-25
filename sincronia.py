import asyncio

async def tarea(nombre):
    print("Iniciando la tareas: ", nombre)
    await asyncio.sleep(2)
    print("Final de la tarea ",nombre)

async def tareasCompletas():
    #Ejecutar las tareas
    await asyncio.gather(
        tarea("Tarea1"),
        tarea("Tarea2"),
        tarea("Tarea3"),
        tarea("Tarea4"),
        tarea("Tarea5"),
        tarea("Tarea6"),
    )

asyncio.run(tareasCompletas())