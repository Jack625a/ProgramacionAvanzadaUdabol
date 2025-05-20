#DataSet para elecciones nacionales
import pandas as pd

#Paso 1. Crear los datos para el dataset
data={
    "Candidatos":[
        "Jorge Tuto Quiroga",
        "Samuel Doria Medina",
        "Manfred Reyes Villa",
        "Eduardo Del Castillo",
        "Rodrigo Paz",
        "Paulo Rodríguez Folster",
        "Jaime Dunn",
        "Eva Copa",
        "Jhonny Fernández",

    ],
    "Partidos":[
        "Alianza Libre",
        "Alianza Unidad",
        "APB-Súmate",
        "MAS",
        "PDC",
        "ADN",
        "NGP",
        "Morena",
        "UCS",
    ],
    "Votos(%)":[
        45.2,
        35.2,
        12.4,
        16.5,
        30.4,
        2.5,
        10.8,
        12.58,
        2.7,
    ]
}
print(data)
#PASO 2. CREAR EL DATAFRAME
dataFrame=pd.DataFrame(data)

print(dataFrame)

#PASO 3. PROCESAR Y GRAFICAR LOS DATOS
import matplotlib.pyplot as plt

#crear la figura
plt.figure(figsize=(10,6))

#Colores para los graficos
colores=[
    "#E9E6DC","#E0B300","#33E000","#0800FF","#01B2E0",
    "#E00101","#6D08E1","#E10084","#01B2E0"
]
#Definir los colores para la grafica (barras)
plt.bar(dataFrame["Candidatos"],dataFrame["Votos(%)"],color=colores)

#PASO 4. PROCESAMIENTO
plt.title(label="Elecciones Nacionales 2025 Simulacion")
plt.ylabel("Porcentaje de votos (%)")
plt.xlabel("Candidatos")
plt.xticks(rotation=30)

#Mostar los porcentajes
for i, (candidato,votos)in enumerate(zip(dataFrame["Candidatos"],dataFrame["Votos(%)"])):
    plt.text(i,votos+1,f"{votos:.1f}%",ha="center")

plt.grid(axis="y",linestyle="--",alpha=0.6)
#Paso 5. mostrar la grafica
plt.tight_layout()
plt.show()

