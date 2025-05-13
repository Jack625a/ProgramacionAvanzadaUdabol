import matplotlib.pyplot as plt
import random

#Simulacion de lectura de datos de un sensor, 
def sensor():
    return random.uniform(12.0,60.0)

x=[]
y=[]

plt.ion()
figura,ax=plt.subplots()

#bucle para la prediccion de datos
for i in range(20):
    valor=sensor()
    x.append(i)
    y.append(valor)

    ax.clear()
    ax.plot(x,y, label="Sensor de Humedad")
    ax.legend()
    ax.set_title("Vizualizacion de Datos en Tiempo Real")
    plt.pause(2)