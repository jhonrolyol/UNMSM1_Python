
# While
'''
Periodo = 2008
while Periodo <= 2015:
    print(f'Informe del año {Periodo}')
    Periodo += 1
'''

''' EJERCICIO:
Escribir un programa que calcule los números
divisibles por 7 que se encuentran entre 
1500 y 2500 e indicar cuales son: 
   Para resolver considerar las variables Min,
   Max y Divisor.
'''

# SOLUCIÓN
Min = 1500
Max = 2500
Divisor = 7
print(f"Los números del {Min} al {Max} que son divisibles por {Divisor} son: ")
Num = Min
while Num <= 2500:
    if (Num % Divisor == 0): # El módulo "%" indica el residuo de una división.
        print(f"El número {Num} es divisible por 7")
    Num += 1
