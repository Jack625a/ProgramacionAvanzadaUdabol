#Introduccion Programacion Orientada a Objetos
#clase (Persona(Nombre, Edad, Ci), Correo)
class Persona:
    #DEFINIR EL CONTRUCTOR
    def __init__(self,nombre,edad,ci,correo):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
        self.correo=correo
    
    #Paso 2. Definir los metodos o acciones
    def comer(self,comida):
        print(f"{self.nombre} esta comiendo {comida}")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

#SUBCLASES (Estudiante)
class Estudiante(Persona):
    #MEtodos o acciones de un estudiante
    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

#Subclase docente (metodo de revisarExamen)
class Docente(Persona):
    def revisarExamen(self,examen):
        print(f"El docente {self.nombre} esta revisando el examen {examen}")

persona1=Persona("Kevin",29,122545,"a@gmail.com")
persona2=Persona("Juan",25,455612,"as@gamil.com")
estudiante1=Estudiante("Rodrigo",22,85545,"ro@gmail.com")

persona1.dormir()
comida=input("Ingrese una comida: ")
persona2.comer(comida)

estudiante1.estudiar()


docente1=Docente("Kevin Arroyo",29,4566,"ass@gmail.com")
examen=input("Ingrese el examen")
docente1.revisarExamen(examen)
docente1.comer("pan")
docente1.dormir()
estudiante1.dormir()