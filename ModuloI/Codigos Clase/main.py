#Esta función realiza la comparación de dos números para ver si son diferentes o iguales
"""
def is_different(num1: int, num2: int) -> bool:
  return True if num1 != num2 else False

my_num1 = float(input('Ingresa un primer número:'))
my_num2 = float(input('Ingresa un segundo número:'))

result = is_different(my_num1, my_num2)

print(result)
print(type(result))

def multiplica_por_3(numero: int) -> int:
  numero = numero*3
  print(numero)
  return numero

multiplica_por_3("hola")


nombre = input('¿Cual es tu nombre?: ')
print('Tu nombre es ',nombre)

#x = 7  #0111
#y = 2  #0011

a = 0b101010
a|= 0b111111
print(bin(a))


# (2**3) (2**2) (2**1) (2**0)
#    0      0     1      0    = 2
#    0      0     1      1    = 3 
#

#PREPARANDO EL ALMUERZO
#TENEMOS 100 PERSONAS
#MIENTRAS LA CANTIDAD DE PERSONAS SEA MENOR O IGUAL A 100 EJECUTO EL PROGRAMA
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()
#YA SUPERÓ LA CANTIDAD DE 100


poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

#VEGETARIANO
poner_agua_hervir()
echar_arroz_hervir()
servir_arroz()

#NO VEGETARIANO
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

#VALOR
x = 10
def funcion(entrada):
    entrada = 0
funcion(x)

print(x) 

#REFERENCIA
x = [10, 20, 30]
def funcion(entrada):
  entrada.append(40)

funcion(x)
print(x)

#id()
x = 10
print(id(x))
def funcion(entrada):
    entrada = 0
    print (id(entrada))
funcion(x)

print(x) 
"""
#id() referencia
x = [10, 20, 30]
print(id(x))
def funcion(entrada):
  entrada.append(40)
  print(id(entrada))
funcion(x)
