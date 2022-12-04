#PROBLEMA 1
# Realizar un programa mediante una función que reciba una muestra de números en una lista y devuelva su media.
"""
La siguiente función recibe el valor de una tupla, estos con valores enteros o decimales. Luego se llama a la función nativa "sum" para realizar la suma, posteriormente utilizaremos la función "len" para dividir entre la cantidad de valores de la cadena recibida, el resultado será la MEDIA
"""

print('****** BIENVENIDOS A CALCULADOR DE MEDIA ******')

def media(*valores):
  resultado = sum(valores) / len(valores)
  return round(resultado,2)

print('La media de los números 5, 10 y 20 es: ', media(5, 10, 20))
