print("Predicciones")
#PASO 1. IMPORTAR LAS LIBRERIAS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#paso 2. datos
data="""Voto,Partido Preferido
Voto 1,MAS
Voto 2,UCS
Voto 3,APB-Súmate
Voto 4,ADN
Voto 5,MAS
Voto 6,Alianza Libre
Voto 7,Morena
Voto 8,MAS
Voto 9,Alianza Unidad
Voto 10,PDC
Voto 11,MAS
Voto 12,Alianza Libre
Voto 13,UCS
Voto 14,NGP
Voto 15,MAS
Voto 16,APB-Súmate
Voto 17,ADN
Voto 18,Alianza Unidad
Voto 19,MAS
Voto 20,Morena
Voto 21,ADN
Voto 22,APB-Súmate
Voto 23,Alianza Libre
Voto 24,MAS
Voto 25,NGP
Voto 26,UCS
Voto 27,MAS
Voto 28,PDC
Voto 29,ADN
Voto 30,Alianza Unidad
Voto 31,MAS
Voto 32,Morena
Voto 33,UCS
Voto 34,ADN
Voto 35,Alianza Libre
Voto 36,MAS
Voto 37,APB-Súmate
Voto 38,PDC
Voto 39,MAS
Voto 40,NGP
Voto 41,Alianza Unidad
Voto 42,MAS
Voto 43,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 50,MAS
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena
Voto 44,ADN
Voto 45,UCS
Voto 46,MAS
Voto 47,Alianza Libre
Voto 48,PDC
Voto 49,Morena

"""

#PASO 3.CONVERTIR EL DATA A DATAFRAME
#importar cadenas de caracteres
from io import StringIO
dataLimpio=pd.read_csv(StringIO(data))

#PASO 4. CONTAR LOS VOTOS
conteoVotos=dataLimpio['Partido Preferido'].value_counts()
print(conteoVotos)

partidos=(
    "MAS",
    "ADN",
    "UCS",
    "Alianza Libre",
    "Morena",
    "PDC",
    "APB-Sumate",
    "Alianza Unidad",
    "NGP"
)

#EXTRA PARA MEJORAR LA PREDICCION
#SIMULACION DE 1000 VOTOS 
simulacion=1000
votosSimulados=100
resultados={partido: 0 for partido in partidos}

for _ in range(simulacion):
    votosSimuladosNuevos=np.random.choice(partidos, size=votosSimulados)
    conteoVotosSimulados=pd.Series(votosSimuladosNuevos).value_counts()
    partidoGandorSimulacion=conteoVotosSimulados.idxmax()


#PASO 6. PREDICCION CON LOS DATOS DEL DATAFRAME
partidoGanador=conteoVotos.idxmax()
votosGanador=conteoVotos.max()
porcentaje=(votosGanador/138)*100

if porcentaje>=51:
    #prediccion
    print(f"Prediccion ganador elecciones {partidoGanador} - {porcentaje}%")
else:
    #prediccion
    print(f"Prediccion Primeros Lugares elecciones {partidoGanador} - {porcentaje}%")



#PASO 5. GRAFICAR
plt.figure(figsize=(8,5))
conteoVotos.plot(kind="bar", color="red")
plt.title("Votos por partidos")
plt.xlabel("Partido")
plt.ylabel("Numero de Votos")
plt.grid(axis='y')
plt.show()


