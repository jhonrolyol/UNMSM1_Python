#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡Hola <nombre>!.

def saludo(nombre):
  """
  Esta función muestra un saludo por la pantalla.
  Parámetros:
  -Nombre: nombre del usuario.
  Devolverá: el saludo => ¡Hola nombre!
  """
  print('¡Hola ' + nombre + '!')
  
print('=====BIENVENIDO=====')
n = input('Ingrese su nombre:')
saludo(n) #Aqui es llamada la función la cual será ejecutada