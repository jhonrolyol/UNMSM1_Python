# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:16:41 2022
@author: GAMER
"""

'''
x = input('Ingrese un numero del 1 al 5:')
x = int(x)
if x == 5:
	print("El número es 5")
else:
  print("El número no es 5")
'''

# Ejercicio
# Hacer un sistema de entrada para que brinde acceso a personas, en caso de ser menor de edad debe prohibirle el ingreso.
# Variables de entrada:
# 1.- Nombre
# 2.- DNI
# 3.- Edad
# Un mensaje de autorización o prohibición.


# Variables de entrada
''' 
Nombre = input("¿Ingrese su nombre?\n")
DNI = int(input("¿Ingrese su número de DNI?\n"))
Edad = int(input("¿Ingrese su edad?\n"))
print("====================")

if Edad < 18 :
	print("====================")
	print("No puede ingresar")
else:
	print("====================")
	print("Puede ingresar")
'''

# EJEMPLO
# CREAR UN PROGRAMA QUE INSERTE DOS NÚMEROS Y
# COMPARE CUAL DE ELLOS ES MAYOR O SI SON
# IGUALES. DEBE INDICAR CUAL ES MAYOR RESPECTO AL OTRO.

'''
num1 = input('Ingresar el valor del primer número:')
num1 = int(num1)
num2 = input('Ingresar el valor del segundo número:')
num2 = int(num2)
print("========================================")
# Comparación 
if num1 == num2:
	print('Los números son iguales y ese número es : {}'.format(num1))
elif num1	< num2:
  print(f'El número {num2} es mayor al número {num1}')
else:
	print(f'El número ', num1, 'es mayor al número', num2)
'''

# EJERCICIO
'''
CREAR UN PROGRAMA QUE PIDA AL USUARIO SU NOMBRE Y 
SU EDAD. 
LAS CONDICIONES SON:
1.- SI LA PERSONA ES MENOR A 18 DE AÑOS, DEBE SOLICITARLE SU CARNÉ CON 1 DOSIS.
2.- SI LA PERSONA TIENE ENTRE 18 A 60 AÑOS, DEBE SOLICITARLE SU CARNÉ CON DOS DOSIS.
3.- SI LA PERSONA TIENE SU EDAD MAYOR A 60 AÑOS,
DEBE SOLICITARLE SU CARNÉ CON LAS TRES DOSIS.
'''

print("====== BIENVENIDO AL PROGRAMA ======")

Nombre = input("¿Digite su nombre:?\n")
Edad = int(input("¿Digite su edad?\n"))

if (Edad >= 5) and (Edad < 18):
    print('Por favor, muestre su carné con una DOSIS')
elif (Edad >= 18 and Edad <= 60):
    print('Por favor, muestre su carné con dos DOSIS')
elif (Edad > 60 and Edad <= 120):
    print('Por favor, muestre su carné con tres DOSIS')
else:
    print('Colocar un número válido')