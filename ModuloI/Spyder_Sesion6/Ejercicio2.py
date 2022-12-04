# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:07:03 2022
@author: GAMER
"""

#%% Ejercicio N° 2
''' EJERCICIO N° 2
Escribir una función que resiba un número 
entero positivo y devuelva su factorial.
'''

#%% Solución 

def Factorial(n):
    '''
    Esta función calcula el factorial de un número
    entero positivo ingresado. 
    Parámetros:
        - n: entero positivo
    Devolver: Factorial de n
    '''
    Temp = 1
    for i in range(n): # n = 4 list(n=4) = [0,1,2,3]
        Temp = Temp*(i + 1)
        # 1 = 1*(0 + 1)
    return Temp    
print('========== FACTORIAL =============')  
x = int(input('Ingrese un número entero positivo: '))
print('El factorial del número', x, 'es', Factorial(x))

  
