import matplotlib.pyplot as plt

#Paso 1. Activar el modo interactivo
plt.ion()

#Paso 2. DATOS DE PRUEBA
x_data=[]
y_data=[]

#Paso 3. Crear los ejes y la grafica
fig,ax=plt.subplots()
line, =ax.plot(x_data,y_data)
ax.set_title("Grafica Dinamica")
ax.set_xlabel("x")
ax.set_ylabel("y")

#DEFINIR LOS LIMITES
ax.set_xlim(0,10)
ax.set_ylim(0,10)

print("Ingrese los datos para la grafica y si desea salir mandar SALIR")
while True:
    datoX=int(input("Ingrese el dato en el eje X: "))
    datoY=int(input("Ingrese el dato en el eje Y: "))
    if datoX=="salir":
        break
    try:
        x_data.append(datoX)
        y_data.append(datoY)

        #graficar
        line.set_xdata(x_data)
        line.set_ydata(y_data)

        #recalcular
        ax.relim()
        ax.autoscale_view()

        plt.draw()
        plt.pause(0,1)
    except Exception as e:
        print("Valores invalidos",e)

plt.ioff()
plt.show()