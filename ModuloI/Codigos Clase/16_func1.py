"""def hello(nombre):
  print('Hola ', nombre)

hello('Juan')
"""
#ARGUMENTO POR POSICION
def suma(a,b):
  print(a+b)
  return 
suma (10,5)

#ARGUMENTOS POR NOMBRE
def resta(a,b):
  print(a-b)

resta (b=5,a=10)

#ARGUMENTACION POR DEFECTO

def suma2(a,b,c=0):
  print(a+b+c)
suma2 (4,5)

#ARGUMENTACION POR VARIABLE
#LISTA
def suma3(numeros):
  print(type(numeros))
  total = 0
  for n in numeros:
    total += n
  print(total)
  return total
suma3([1,2,3,4,5])

#TUPLA
#USANDO *
def suma4(*numeros):
  print(type(numeros))
  total = 0
  for n in numeros:
    total += n
  print(total)
  return total
suma4(1,2,3,4,5,6,7,8,9,10)

#USANDO ** CLAVE Y VALOR A LOS ARGUMENTOS
def suma5(**num):
  suma = 0;
  for key, value in num.items():
    print(key,value)
    suma += value
  print(suma)
  return suma
  
suma5(a=3, b=5, c=8)



