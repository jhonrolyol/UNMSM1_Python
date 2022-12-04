# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:52:55 2022
@author: GAMER
"""

#%% Módulo o module ".py"

import operaciones

print(operaciones.Suma(5,8))
print(operaciones.Resta(9,4))


#%% Uso del from import 

from operaciones import Suma, Resta

print(Suma(4,9))
print(Resta(4,9))

#%% Uso del import*

from operaciones import*
print(Suma(5,8))
print(Resta(9,4))

#%% Rutas
'''
archivo1.py
Carpteta
    archivo2.py
'''    
#%% archivo2.py
def Hola():
    print('Hola')

#%% Archivo.py
from CARPETA.archivo2 import*
print(Hola())
