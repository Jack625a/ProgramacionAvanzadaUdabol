#Tecnicas para la concurrencia
#HILOS (thereading): Trabajo de tareas d forma concurrente
#Modulos para hilos 
import threading
import time

#Simulacion de tareas
def tarea(nombre):
    print("Iniciando la tareas: ", nombre)
    time.sleep(2)#  Simulacion de el completado de la tarea
    print("Final de la tarea ",nombre)

#Tareas
tarea1=tarea("Tarea1")
tarea2=tarea("Tarea2")
tarea3=tarea("Tarea3")
tarea4=tarea("Tarea4")
tarea5=tarea("Tarea5")
tarea6=tarea("Tarea6")
tarea7=tarea("Tarea7")
tarea8=tarea("Tarea8")
tarea9=tarea("Tarea9")
tarea10=tarea("Tarea10")

#CREACION DE LOS HILOS
hilo1=threading.Thread(target=tarea1, args=("Hilo 1"))
hilo2=threading.Thread(target=tarea2, args=("Hilo 2"))
hilo1.start()
hilo2.start()

#EJECUTAR EL PROCESAMIENTO SIMULTANEI
hilo1.join()
hilo2.join()

print("Tareas finalizadas..")