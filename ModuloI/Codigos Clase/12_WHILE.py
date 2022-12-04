"""#WHILE
periodo = 2008

while periodo <= 2015:
  print(f'Informe del año {periodo}')
  periodo += 1
"""

#EJERCICIO
#Escribir un programa que calcule los numeros divisibles por 7 que se encuentren 1500 y 2500, indicar cuales son:

min = 1500
max = 2500
divisor = 7

print('Los números del {} al {} divisibles por {}'.format(min, max, divisor))
num = min
while num <= 2500:
  if (num % divisor == 0):
    print('El número {} es divisible por 7'.format(num))
  num +=1


