# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:05:40 2022
@author: GAMER
"""

#%% Creamos la función "hello()"

def hello():
    print('Hola')
hello() # Llamamos a la función

#%% Creamos la función "hello(Nombre)"

def hello(Nombre): # En este caso usamos un parámetro o variable dentro de la función
    print('Hola', Nombre)
hello('Juan')  # Llamamos a la función

#%% Argumentos por posición 

def suma(a,b):
    print(a + b)
    return  # Sin el "return" también sale el resultado
suma(10,5)  # Llamamos a la función

#%% Argumentos por nombres

def resta(a,b):
    print(a - b)
resta(5,10)  # Llamamos a la función
resta(b = 5,a = 10)  # Llamamos a la función indicando el argumento

#%% Argumentos por defecto 

def suma2(a,b, c = 0): # c = 0 es fijo
    print(a + b + c)
suma2(4,5)

def suma2(a,b, c = 6): # c = 6 es fijo
    print(a + b + c)
suma2(4,5)   

#%% Argumento de longitud variable 
# Usando una Lista

def suma3(numeros):
    print(type(numeros))
    total = 0
    for n in numeros:
        total += n
    print(total)
    return total 
suma3([1,2,3,4,5])

#%% Tupla
# Usando "*"
def suma4(*numeros): # El asterico ayuda a convertir en una tupla
    print(type(numeros))
    total = 0
    for n in numeros:
        total += n
        print(total)
        return total 
suma4(1,2,3,4,5,6,7,8,9,10) # Se puede usar la cantidad que se quiere

#%% Tupla
# Usando "**" se puede usar "clave y valor" en los argumentos

def suma5(**num):
    suma = 0
    for key, value in num.items():
        print(key,value)
        suma += value
    print(suma)
    return suma
suma5(a = 3, b = 5, c = 8) # Llamamos a la función
        