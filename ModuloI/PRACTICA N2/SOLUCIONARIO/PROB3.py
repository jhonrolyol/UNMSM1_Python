#PROBLEMA 3
#Realizar un programa que incluya una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""
La siguiente función realiza la validación de la cantidad de dígitos de un DNI ingresado, para ello utilizaremos la función "len" para obtener el dato de la cantidad de valores del DNI, posteriormente haremos una condicional para indicar si el documento es VÁLIDO o NO.
"""
print('****** VALIDACIÓN DE DNI ******')

def validarDNI(dni):
  extension = len(dni)
  if extension == 7 or extension == 8:
    resultado = True
  else:
    resultado = False
  return resultado

documento = input('Ingrese su número de DNI: ')
print('El DNI ingresado es: ',validarDNI(documento))