# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:20:56 2022
@author: GAMER
"""

#%% Programación Orientada a Objetos
# Ejemplo: Mascota = perrito
# Clases
# Atributos
# Métodos
# Objeto
  ## Principios
     ### Herencia
     ### Cohesión
     ### Abstracción
     ### Polimorfismo
     ### Acoplamiento
     ### Encapsulado
     
#%% Creamos una clase
class Perro:
    pass 

MiPerro = Perro()

#%% Atritbuto de instancia
class Perro:
    def __int__(self, Nombre,Raza):
        print(f'Creando perro {Nombre}, {Raza}')
        self.Nombre = Nombre
        self.Raza = Raza
MiPerro = Perro('Firulais', 'Chihuahua')
print(type(MiPerro))        

print(MiPerro.Raza)
print(MiPerro.Nombre)

#%% Atributo de clase
class Perro:
    Especie = 'Manífero'
    def __init__(self, Nombre,Raza):
        print(f'Creando perro {Nombre}, {Raza}')
        self.Nombre = Nombre
        self.Raza = Raza
print(Perro.Especie)        

MiPerro = Perro('Firulais', 'Chihuahua')
MiPerro.Especie

#%% Métodos
class Perro:
    Especie = 'Manífero'
    def __init__(self, Nombre,Raza):
        print(f'Creando perro {Nombre}, {Raza}')
        self.Nombre = Nombre
        self.Raza = Raza
        
    def Ladra(self):
        print('Guau')
        
    def Camina(self, Pasos):
        print(f'Camina {Pasos} pasos')
        
    def Truco(self):
        print('Se sienta')

MiPerro = Perro('Firulais', 'Chihuahua')
MiPerro.Ladra()
MiPerro.Camina(20)
MiPerro.Truco()

#%% Herencia
# Clase padre
class Animal:
    pass 
# Clase hija
class Perro(Animal):
    pass
# __bases__ para visualizar la clase padre
print(Perro.__bases__)
# __subclasses__ para visualizar la clases hijas
print(Animal.__subclasses__())

# Filosofía DRY - Don't Repeat Yourself
# Creamos una clase padre la cuál tendrá dos atributos: Especie y Edad
# Creemos métodos o funcionalidades: Hablar y Moverse

# Clase padre
class Animal:
    def __init__(self, Especie, Edad):
        print(f'Creando animal de especie {Especie} y {Edad} años de edad')
        self.Especie = Especie
        self.Edad = Edad
        
    def Hablar(self):
        pass
    
    def Moverse(self):
        pass
# Clase hija    
class Perro(Animal):
    def Hablar(self):
        print('Guau')
    def Moverse(self):
        print('Camina en 4 patas')
class Gato(Animal):
    def Hablar(self):
        print('Miau')
    def Moverse(self):
        print('Camina en 4 patas')
    def Defensa(self):
        print('Este animal araña')
class Paloma(Animal):
    def Hablar(self):
        print('Arulla')
    def Moverse(self):
        print('Vuela')
    
        
# Creo un objeto
MiPerro = Perro('Manífero', '15')
MiGato = Gato('Manífero', '7')
MiPaloma = Paloma('Ave', '2')

# Llamar al método
MiPerro.Hablar()
MiGato.Defensa()
MiPaloma.Moverse()


# Super()
class Animal:
    def __init__(self, Especie, Edad):
        print(f'Creando animal de especie {Especie} y {Edad} años de edad')
        self.Especie = Especie
        self.Edad = Edad
        
    def Hablar(self):
        pass
    
    def Moverse(self):
        pass
# Opción 1    
class Perro(Animal):
    def __init__(self, Especie, Edad, Dueño):
        print(f'Creando un animal {Especie}, con {Edad} años de edad, cuyo dueño es {Dueño}')
        self.Especie = Especie
        self.Edad = Edad
        self.Dueño = Dueño
MiPerro = Perro('Manífero', '15','Juanito')
MiPerro.Especie
MiPerro.Edad
MiPerro.Dueño
        
# Opción 2    
class Perro(Animal):
    def __init__(self, Especie, Edad, Dueño):
        super().__init__(Especie, Edad, Dueño)
        self.Dueño = Dueño
      
    
