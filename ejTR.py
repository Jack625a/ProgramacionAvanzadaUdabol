from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
dataset = load_dataset("aswin1906/countries-inflation", split="train")
df = dataset.to_pandas()

# Convertir columnas a numérico
df["Available data"] = pd.to_numeric(df["Available data"], errors='coerce')
df["Inflation, 2022"] = pd.to_numeric(df["Inflation, 2022"], errors='coerce')

# Eliminar nulos
df = df.dropna(subset=["Available data", "Inflation, 2022", "Global rank"])

# Países a graficar
paises = ["Bolivia", "Argentina", "Colombia", "Brazil"]

# Si un país no tiene datos suficientes, añadir un punto manualmente
for pais in paises:
    datos_pais = df[df["Countries"] == pais]
    if datos_pais.empty or len(datos_pais) < 1:
        nuevo = {
            "Countries": pais,
            "Available data": 2022,
            "Inflation, 2022": 5.0,  # Valor ficticio
            "Global rank": 100       # Valor ficticio
        }
        df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)

# GRAFICAR
plt.figure(figsize=(12, 6))

for pais in paises:
    datos = df[df["Countries"] == pais].sort_values(by="Available data")
    
    plt.scatter(datos["Available data"], datos["Inflation, 2022"], label=pais, s=70)
    
    for x, y, rank in zip(datos["Available data"], datos["Inflation, 2022"], datos["Global rank"]):
        plt.text(x, y, str(rank), fontsize=8, ha='right', va='bottom')

plt.title("Inflación de países (puntos con valores añadidos)")
plt.xlabel("Año")
plt.ylabel("Inflación (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
