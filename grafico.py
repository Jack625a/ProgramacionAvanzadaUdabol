import matplotlib.pyplot as plt
import random

x=[random.uniform(0,30) for _ in range(100)]
y=[2*i+random.uniform(-2,2)for i in x]

#crear el grafico
plt.scatter(x,y,color='red',label="Datos")
plt.title("Grafico de dispersiones")
plt.xlabel("Valores x")
plt.ylabel("Valores y")
plt.legend()
plt.grid(True)
plt.show()