# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:55:48 2022
@author: GAMER
"""

#%% VALOR

x = 10
def funcion(entrada):
    entrada = 0
    return entrada
funcion(x)    
print(x) # 10

#%% REFERENCIA

x = [10,20,30]
def funcion(entrada):
    entrada.append(40)
funcion(x)
print(x)

#%% id()

x = 10
print(id(x)) # Muestra el identificador único
def funcion(entrada):
    entrada = 0
    print(id(entrada))
funcion(x)
print(x)

#%% id() para referencia

x = [10,20,30]
print(id(x))
def funcion(entrada):
    entrada.append(40)
    print(id(entrada))
funcion(x)



