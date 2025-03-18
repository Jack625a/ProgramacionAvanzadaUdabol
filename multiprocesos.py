#Programacion en Paralelo
#Multiprocesos ()
# Modulo de multiprocesos
import multiprocessing #Importar el modulo
#Importacion de un reloj para realizar la simulacion
import time

class PruebaProcesos:
    #Paso2 Definir el constructor
    def __init__(self,nombre):
        self.nombre=nombre

    def crearTarea(self):
        print(F"SE CREO LA TAREA a nombre de {self.nombre}")
        #Modulo time para simular el trabajo
        time.sleep(2)
        print("Se completo la tarea")

    def ejecutarTarea(self):
        tareas=[]
        tareas2=[]
        for i, tarea in enumerate(self.nombre):
            p1=multiprocessing.Process(target=tarea)
            p2=multiprocessing.Process(target=tarea)
            tareas.append(p1)
            tareas2.append(p2)
            tareas.start()


if __name__== '__main__':
    tarea1=PruebaProcesos("prueba1")
    tarea2=PruebaProcesos("Prueba2")

    proceso1=multiprocessing.Process(target=tarea1.crearTarea())
    proceso2=multiprocessing.Process(target=tarea2.crearTarea())


    #Simulacion de la ejecucion del proceso
    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.join()
    print("Proceso completos")

