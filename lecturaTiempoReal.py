#simulacion de lectura de datos para analiis
#PANDAS pip install pandas
#Importaciones de las bibliotecas
import pandas as pd
import time
import random

#Simulacion de lectura de datos de un sensor, 
def sensor():
    return random.uniform(10.0,50.0)

#Almacenar los datos
datos=[]
#Simulacion de 20 lecturas
for _ in range(20):
    registro=sensor()
    tiempo=time.strftime("%H:%M:%S")
    añadir=f" hora: {tiempo} - sensor: {registro}"
    datos.append(añadir)
    analizar=pd.DataFrame(datos)
    print(analizar.tail(1))
    time.sleep(1)

