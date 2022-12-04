# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:22:12 2022
@author: GAMER
"""

#%% Lista1
Lista1 = [1,2,3,4]
print(Lista1)

#%% Lista2
Lista2 = list("1234")
print(Lista2)

#%% Lista3
Lista3 = [1,"Juan",3.1415,[1,2]]
print(Lista3)

#%% Ubicar un elemento de la lista con índice.
print(Lista3[1])
print(Lista3[3])
print(Lista3[-1])
print(Lista3[-2])

#%% Borrar un elemento de la lista con índice
del Lista3[1]
print(Lista3)
print(Lista3[1])
print(Lista3[2][0]) # Acceder al elemento de una lista que está dentro de otra lista.

#%% Lista4
Lista4 = [1,2,3,4,5,6]
print(Lista4[0:2]) # Muestra hasta antes de la ubicación 2.
print(Lista4[2:4])

Lista4[0:4] = [10,20,30,40] # Remplazar con nuevos valores.
print(Lista4)
