#Paso 1. Importacion de las librerias
from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#Paso 2. Cargar el dataset
dataset=load_dataset("aswin1906/countries-inflation", split="train")
dataframe=dataset.to_pandas()

#Paso 3. Convertir los datos en representacion numerica
dataframe["Available data"]=pd.to_numeric(dataframe["Available data"],errors="coerce") #conversion del año
dataframe["Inflation, 2022"]=pd.to_numeric(dataframe["Inflation, 2022"],errors="coerce") #conversion del valor de la inflacion
dataframe["Global rank"]=pd.to_numeric(dataframe["Global rank"],errors="coerce") #conversion del dato ranking

#Paso 4. lista de paises
paises=["Bolivia","Argentina","Colombia","Brazil","Costa Rica","Panama","Chile"]
#aumenar los años
años=list(range(2022,2025))

#Paso 5. Complementar los datos faltantes
for pais in paises:
    datosPaises=dataframe[dataframe["Countries"]==pais]
    faltantes=20-len(datosPaises)
    if faltantes>0:
        añosSeleccionados=datosPaises["Available data"].tolist()
        añosDisponibles=[a for a in años if a not in añosSeleccionados]
        nuevos=[]
        for _ in range(faltantes):
            año=np.random.choice(añosDisponibles)
            inflacion=np.round(np.random.uniform(1,140),2)
            ranking=np.random.randint(1,150)
            nuevos.append({
                "Countries":pais,
                "Available data":año,
                "Inflation, 2022":inflacion,
                "Global rank":ranking
            })

añosDisponibles.remove(año)
dataframe=pd.concat([dataframe,pd.DataFrame(nuevos)])

#Paso 6. Graficar
plt.figure(figsize=(20,8))

for pais in paises:
    datos=dataframe[dataframe["Countries"]==pais]
    plt.scatter(datos["Available data"],datos["Inflation, 2022"], label=pais)
    for x,y,ranking in zip(datos["Available data"],datos["Inflation, 2022"],datos["Global rank"]):
        plt.text(x,y,str(ranking),fontsize=8)


#Armar el grafico
plt.title("Inflacion en 7 paises")
plt.xlabel("Año")
plt.ylabel("Inflacion %")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()