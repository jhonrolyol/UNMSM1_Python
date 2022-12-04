# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 07:06:29 2022
@author: GAMER
"""

#%% Return 
# Creamo a "mi_funcion()"
def mi_funcion():
    print('Inicio de la función')
    return
    print('Esto no se muestra')    
mi_funcion()
    
#%% Creamos a "suma_media()"
def suma_media(a,b,c):
    suma = a + b + c
    media = suma/3
    return suma, media # Cuando hay más de uno usar comas
suma,media = suma_media(5,10,15)
print(suma)
print(media)

#%% Ayuda o documentación
help()
print(suma_media.__doc__)

## Multiplicación

def multiplica_por_3(numero: int) -> int: 
    numero = numero*3
    print(numero)
    return numero
multiplica_por_3('Hola') # Llamamos a la función


