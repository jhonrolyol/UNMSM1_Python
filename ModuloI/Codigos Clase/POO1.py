#PROGRAMACION ORIENTADA A OBJETOS
#EJ, mascota: perrito
#CLASES
#ATRIBUTOS
#METODOS
#OBJETO
  #PRINCIPIOS:
  #HERENCIA
  #COHESION
  #ABSTRACCION
  #POLIMORFISMO
  #ACOPLAMIENTO
  #ENCAPSULIDAD

#Creamos una clase
"""
class Perro:
  pass

mi_perro = Perro()

#Atributo de instancia
class Perro:
  def __init__(self,nombre,raza):
    print(f'Creando perro {nombre}, {raza}')
    self.nombre = nombre
    self.raza = raza

mi_perro = Perro('Firulais', 'chihuahua')
print(type(mi_perro))

print(mi_perro.raza)
print(mi_perro.nombre)

#Atributo de clase
class Perro:
  especie = 'mamífero'
  def __init__(self,nombre,raza):
    print(f'Creando perro {nombre}, {raza}')
    self.nombre = nombre
    self.raza = raza

print(Perro.especie)
mi_perro = Perro('Firulais', 'chihuahua')
print(type(mi_perro))

#MÉTODOS
class Perro:
  especie = 'mamífero'
  def __init__(self,nombre,raza):
    print(f'Creando perro {nombre}, {raza}')
    self.nombre = nombre
    self.raza = raza

  def ladra(self):
    print('Guau')

  def camina(self, pasos):
    print(f'Camina {pasos} pasos')

  def truco(self):
    print('Se sienta')

mi_perro = Perro('Firulais','chihuahua')
mi_perro.ladra()
mi_perro.camina(20)
mi_perro.truco()
"""

#HERENCIA
#Clase padre
class Animal:
  pass
#Clase hija
class Perro(Animal):
  pass
#__bases__ => para visualizar la Clase Padre
print(Perro.__bases__)
#__subclasses__ => para visualizar clases hijas
print(Animal.__subclasses__())

#FILOSOFIA DRY - Don't Repeat Yourself
#Creamos una clase padre la cual tendrá dos atributos: Especie y edad.
#Creamos métodos o funcionalidades: hablar y moverse.
#CLASE PADRE
class Animal:
  def __init__(self, especie, edad):
    #print(f'Creando animal de especie {especie} y {edad} años de edad')
    self.especie = especie
    self.edad = edad

  def hablar(self):
    pass

  def moverse(self):
    pass

#CLASE HIJA
class Perro(Animal):
  def hablar(self):
    print('Guau')
  def moverse(self):
    print('Camina en 4 patas')

class Gato(Animal):
  def hablar(self):
    print('Miau')
  def moverse(self):
    print('Camina en 4 patas')
  def defensa(self):
    print('Este animal araña')
    
class Paloma(Animal):
  def hablar(self):
    print('arrulla')
  def moverse(self):
    print('Vuela')

#CREO UN OBJETO
mi_perro = Perro('mamifero','15')
mi_gato = Gato('mamífero','7')
mi_paloma = Paloma('ave','2')

#LLAMAR AL MÉTODO se llama con el "." luego del objeto
mi_perro.hablar()
mi_gato.defensa()
mi_paloma.moverse()

#SUPER()
class Animal:
  def __init__(self, especie, edad):
    #print(f'Creando animal de especie {especie} y {edad} años de edad')
    self.especie = especie
    self.edad = edad

  def hablar(self):
    pass

  def moverse(self):
    pass

#opcion 1
"""
class Perro(Animal):
  def __init__(self, especie, edad, dueño):
    print(f'Creando un animal {especie}, con {edad} años de edad, cuyo dueño es {dueño}')
    self.especie = especie
    self.edad = edad
    self.dueño = dueño

mi_perro = Perro('mamífero','15','Juanito')
mi_perro.especie
mi_perro.edad
mi_perro.dueño
"""
#opcion 2
class Perro(Animal):
  def __init__(self, especie, edad):
    super().__init__(especie, edad)
    self.dueño = dueño

