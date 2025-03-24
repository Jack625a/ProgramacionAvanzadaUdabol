#Eje1. Renderizado y control de brillo para imagenes en simultaneo
#Modulo Multiprocesos

#Paso 1. Importacion de modulos

import multiprocessing #Procesamiento en paralelo
import os #manejar las rutas del sistema oeprativo
from PIL import Image, ImageEnhance


#Paso 2. Crear la clase
class ProcesarImagen:
    #definir el constructir
    def __init__(self,rutaIamgen,salidaImagen,efectos):
        self.rutaImagen=rutaIamgen
        self.salidaImagen=salidaImagen
        self.efectos=efectos

    #Paso 3. Crear los metodos de la clase
    def procesar(self):
        imagen=Image.open(self.rutaImagen)#Abre  la imagen desde la ruta indicada
        cambio=ImageEnhance.Brightness(imagen)
        imagenModificada=cambio.enhance(self.efectos) #Aplicar los efectos a la imagen (brillo)
        imagenModificada.save(self.salidaImagen)



#Metodo para procesar las imagenes en paralelo
def procesaImagenParalelo(imagenes):
    procesos=[] 
    #Crear un bucle iterativo para procesar las imagenes
    for image in imagenes:
        procesamiento=multiprocessing.Process(target=image.procesar)
        procesos.append(procesamiento)
        procesamiento.start()
    #El procesamiento de todas las imagenes en espera del proceso
    for procesamiento in procesos:
        procesamiento.join()


#Objetos de la clase


if __name__== '__main__':
    listaImagenes=[ProcesarImagen("imagenes\PythonLogo.png","salida1.png",1.5),ProcesarImagen("imagenes\JavaScript-logo.png","salida2.png",0.5),ProcesarImagen("imagenes\javaLogo.png","salida3.png",1.9)]
    procesaImagenParalelo(listaImagenes)