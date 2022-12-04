# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:24:36 2022
@author: GAMER
"""


#%% Uso de "try" y "except"

a = int(input('Ingrese en dividendo'))
b = int(input('Ingrese el divisor'))
# a = 4
# b = 0

try:
    c = a/b
    x = 3 + '2'
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except TypeError:
    print('No se puede operar diferentes tipos')    
    
print('Hello')

#%% else


a = int(input('Ingrese en dividendo'))
b = int(input('Ingrese el divisor'))

try:
    x = a/b
except:
    print('La división entre 0 no se puede operar')
else:
    print('No ha ocurrido alguna excepción')           

#%% finally
a = int(input('Ingrese en dividendo'))
b = int(input('Ingrese el divisor'))

try:
    x = a/b
except: 
    print('Entre en except, ha ocurrido una excepción') 
finally:
    print('Pasa si o si por este por este bloque')

#%% Ejemplo 
try:
    with open('fichero.txt') as file:
        read_data = file.read()
except:
    print('No se puede abrir')        


