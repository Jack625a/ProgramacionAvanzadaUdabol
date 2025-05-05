#Paso 1. Importar la liberia
import dask
import time

#Paralelismo con funciones basica
#dask.delayed
@dask.delayed 
def restar(a,b):
    return a-b

@dask.delayed
def sumar(a,b):
    return a+b
#ejecutar las funciones
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
suma=sumar(a,b)
resta=restar(a,b)
calculos=suma.compute()
resultado=resta.compute()
print(f"Resultado de la suma es: {calculos} - Resuktado de la resta es: {resultado}")