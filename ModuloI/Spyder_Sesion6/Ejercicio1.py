# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:14:20 2022
@author: GAMER
"""

#%% Ejercicio N° 1
''' EJERCICIO N° 1
Escribir una función a la que se le pase una
cadena <nombre> y muestre por pantalla
el saludo, ¡Hola,<nombre>! 
'''

#%% Solución

def Saludo(Nombre):
    '''
    Esta función muestra un saludo por pantalla.
    Parámetros:
        - Nombre: nombre de usuario.
    Devolverá: el saludo => ¡Hola, nombre!
        
    '''
    print('¡Hola, ' + Nombre + '!')
    return 
print('=========== BIENVENIDO ============')
n = input('Ingrese su nombre: ')
Saludo(n) # Aquí es llamada la función la cual será ejecutada.

