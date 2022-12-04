#MANEJO DE EXCEPCIONES
#raise ZeroDivisionError('Información de la excepción')
#raise TypeError('Información de la excepción')
#USO DE TRY EXCEPT
"""
a = int(input('Ingrese el Dividendo: '))
b = int(input('Ingrese el divisor: '))
#a = 4
#b = 0

try:
  c = a / b
  x = 3 + '2'
except ZeroDivisionError:
  print('No se puede dividir entro 0')
except TypeError:
  print('No se puede operar diferentes tipos')

print('Hello')

#ELSE
a = int(input('Ingrese el Dividendo: '))
b = int(input('Ingrese el divisor: '))
try:
  x = a / b
except:
  print('La división entre 0 no se puede operar')
else:
  print('No ha ocurrido alguna excepción')
  """
#FINALLY
a = int(input('ingrese un valor: '))
b = int(input('ingrese un valor: '))
try:
  x = a/b
except:
  print('Entre en except, ha ocurrido una excepción')
finally:
  print('Pasa si o sí por este bloque')

#Ejemplo:
try:
  with open('fichero.txt') as file:
    read_data = file.read()
except:
  print('No se pudo abrir')


  
  
#if b != 0:
#print (a / b)
#else:
 # print('No se puede dividir')
#c = a / b
#print (c)
#print (2 + '3')

#USO DE RAISE
