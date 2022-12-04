# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:24:01 2022
@author: GAMER
"""

#%% Ejercicio N° 3
''' EJERCICIO N° 3
Escribir una función que calcule el máximo comun divisor 
de dos números y otra que calcule el mínimo común multiplo.
'''

#%% Solución mcd

def mcd(a,b):
    '''
    Esta función calcula el máximo
    común divisor de dos números.
    Parámetros:
        - a y b números enteros.
    Devolver: El mcd de a y b
    '''
    Resto = 0
    while (b > 0):
        Resto = b
        b = a%b
        a = Resto
    return a
print('============== MCD ==============')    
x = int(input('Ingrese un primer número: '))
y = int(input('Ingrese un segundo número: '))
print('El mcd de',x,'y',y,'es',mcd(x,y))

#%% Solución mcm

def mcm(a,b):
    '''
    Esta función calcula el mínimo comun múltiplo de dos números.
    Parámetros:
        - a y b : números enteros
    Devolver: el mcm de a y b 
    '''
    if a > b :
        Mayor = a
    else:
        Mayor = b
        
    while (Mayor%a != 0) or (Mayor%b != 0):
        Mayor = Mayor + 1
    return Mayor 
print('============== MCM ==============')    
x = int(input('Ingrese un primer número: '))
y = int(input('Ingrese un segundo número: '))
print('El mcm de',x,'y',y,'es',mcm(x,y))        

