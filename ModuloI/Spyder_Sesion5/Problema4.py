# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 05:54:06 2022
@author: GAMER
"""

#%% Problema 10 "Solución de Alvaro Achas"
print('===============================')
print(' ')
print('    ECUACIONES DE PRIMER GRADO ')
print(' ')
print('===============================')
print(' ')

print('Primero, escriba su ecuación lineal de la siguiente forma: ax + b = c')

print(' ')

a = float(input('Introducir el valor de "a": '))
b = float(input('Introducir el valor de "b": '))
c = float(input('Introducir el valor de "c": '))

print(' ')
print('====================================')
print(' ')

if a == 0:
    print('La ecuación no presenta solución debido a que "a=0"')
else:
    x = float((c-b)/a)
    x1 = round(x,2)
    print(f'La solución redondeada a dos decimales de la ecuación lineal es {x1}')

print(' ')    
print('===============================')
 

#%% Problema 10 "Solución de Luis Fabian"
print("Calcula tus ahorros anuales")
print("============================")
deposito = float(input("Por favor, ingrese la cantidad de dinero a depositar: "))
interes = 0.05
ahorro1 = deposito*(1 + interes)
print("Tu ahorro en el primer año es: " + str(round(ahorro1,2)))
ahorro2 = ahorro1*(1 + interes)
print("Tu ahorro en el segundo año es: " + str(round(ahorro2,2)))
ahorro3 = ahorro2*(1 + interes)
print("Tu ahorro en el tercer año es: " + str(round(ahorro3,2)))

