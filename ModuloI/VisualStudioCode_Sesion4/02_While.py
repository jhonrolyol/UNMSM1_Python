# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:41:17 2022
@author: GAMER
"""

#%% While
Periodo = 2008
while Periodo  <= 2015:
    print(f'Informe del año {Periodo}')
    Periodo += 1

#%% EJERCICIO
''' EJERCICIO:
Escribir un programa que calcule
los números divisibles por 7
que se encuentren entre 1500 y 2500,
indicar cuales son:
    Min
    Max
    Divisor
'''

#%% TEORÍA
''' RECORDEMOS UN POCO DE TEORÍA:
Para saber si un número es divisible entre 7 
hay que restar el número sin la cifra de las 
unidades y el doble de la cifra de las unidades. 
Si el resultado es 0 o múltiplo de 7 entonces 
el número es divisible entre 7.
'''



#%% INTENTO 
print("======= BIENVENIDO AL PROGRAMA ======")
x = 1500 # Definimos el valor mínimo.
y = 2500 # Definimos el valor máximo.
d = 7 # Definimos el divisor.
print(f"Los números del {x} al {y} que son divisibles por {d} son: ")
while (x <= y):
    if (x % d == 0): # El módulo "%" indica el residuo de una división.
        print(f'El número {x} es divisible por 7')
    x += 1


#%% SOLUCIÓN 
Min = 1500
Max = 2500
Divisor = 7
print("Los números del {} al {} divisibles por {}".format(Min,Max,Divisor))
Num = Min
while Num <= 2500: 
    if (Num % Divisor == 0): # El módulo "%" indica el residuo de una división.
        print('El número {} es divisible por 7'.format(Num))
    Num += 1

