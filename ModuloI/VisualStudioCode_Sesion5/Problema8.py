# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 05:53:57 2022
@author: GAMER
"""

#%% PROBLEMA 8 "Solcuión de Cynthia Cornejo"
# Programa que valida si el número es par o impar
numero = int(input('Ingrese un número: '))
if numero%2 == 0:
    print('El número es par')
else:
    print('El número es impar')
continuar = input('Desea continuar Si o No?: ')    

while continuar == 'Si':
    numero = int(input('Ingrese un número: '))
    if numero%2 == 0:
        print('El número es par')
    else:
        print('El número es impar')   
    continuar = bool(input('Desea continuar Si o No?: '))

#%% Problema 8  "Solución de Hussein Palomino" 
print("===================================")
consulta = 'SI'
while consulta == 'SI':
    numero = int(input('Ingrese un número a consultar: '))
    if numero%2 == 0:
        print('El número es par')
    else:
        print('El número es impar')
    print("=====================")
    print("Digite 'SI' para continuar o 'NO' para terminar el proceso")
    consulta = input("¿Desea seguir consultando?: ").upper()
print("=========================")
print("Se terminó el proceso")
