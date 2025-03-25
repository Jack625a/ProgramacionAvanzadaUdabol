#Eje1. Renderizado y control de brillo para imagenes en simultaneo
#Modulo Multiprocesos

#Paso 1. Importacion de modulos

import multiprocessing  # Procesamiento en paralelo
import os  # Manejar rutas del sistema operativo
from PIL import Image, ImageEnhance

# Paso 2. Crear la clase
class ProcesarImagen:
    def __init__(self, rutaImagen, salidaImagen, efectos):
        self.rutaImagen = rutaImagen
        self.salidaImagen = salidaImagen
        self.efectos = efectos

    def procesar(self):
        """Aplica efectos de brillo a la imagen y la guarda en la salida especificada."""
        try:
            if not os.path.exists(self.rutaImagen):
                print(f"Error: No se encontró la imagen {self.rutaImagen}")
                return

            print(f"Procesando {self.rutaImagen} con efecto de brillo {self.efectos}...")
            imagen = Image.open(self.rutaImagen)  # Abrir imagen
            cambio = ImageEnhance.Brightness(imagen)
            imagenModificada = cambio.enhance(self.efectos)  # Aplicar efecto
            imagenModificada.save(self.salidaImagen)  # Guardar imagen modificada
            print(f"Imagen procesada y guardada en {self.salidaImagen}")
        except Exception as e:
            print(f"Error procesando {self.rutaImagen}: {e}")

# Método para procesar imágenes en paralelo
def procesaImagenParalelo(imagenes):
    procesos = []
    for image in imagenes:
        procesamiento = multiprocessing.Process(target=image.procesar)
        procesos.append(procesamiento)
        procesamiento.start()

    for procesamiento in procesos:
        procesamiento.join()

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn', force=True)  # Compatibilidad con Windows

    carpeta_imagenes = "imagenes"
    listaImagenes = [
        ProcesarImagen(os.path.join(carpeta_imagenes, "PythonLogo.png"), "salida1.png", 1.5),
        ProcesarImagen(os.path.join(carpeta_imagenes, "JavaScript-logo.png"), "salida2.png", 0.5),
        ProcesarImagen(os.path.join(carpeta_imagenes, "logojava.jpg"), "salida3.png", 1.9),
        ProcesarImagen(os.path.join(carpeta_imagenes,"c++Logo.png"),"salida4.png",0.8)
    ]

    procesaImagenParalelo(listaImagenes)
    print("Procesamiento de imágenes finalizado.")