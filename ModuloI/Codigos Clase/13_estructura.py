"""
x = input('Ingrese un número del 1 al 5:')
x = int(x)
print(type(x))
if x == 5:
  print("El número es 5")
else:
  print('El número no es 5')


#Ejercicio:
Hacer un sistema de entrada para que brinde acceso a personas, en caso de ser menor de edad debe prohibirle el ingreso.
Variables de entrada:
1. Nombre
2. DNI
3. Edad

Salida: Un mensaje de autorización o prohibición.


print('BIENVENIDO AL SISTEMA DE AUTORIZACIÓN:')
print("=============================")
nombre = input('Por favor, ingrese su nombre: ')
dni = input('Por favor, ingrese su número de dni: ')
dni = int(dni)
edad = int(input('Por favor, ingrese su edad: '))

if edad < 18:
  print("=============================")
  print(f'La persona con nombre {nombre} y dni {dni} NO PUEDE INGRESAR POR SER MENOR DE EDAD')
else:
  print("=============================")
  print(f'La persona con nombre {nombre} y dni {dni} SI PUEDE INGRESAR')

 
#EJEMPLO:
#CREAR UN PROGRAMA QUE INSERTE DOS NUMEROS Y COMPARE CUAL DE ELLOS ES MAYOR O SI SON IGUALES.DEBE INDICAR CUAL ES MAYOR RESPECTO AL OTRO.

#Insertar valores
num1 = input('Ingresar el valor del primer número:')
num1 = int(num1)
num2 = input('Ingresar el valor del segundo número: ')
num2 = int(num2)
print('------------------------')
#comparación
if num1 == num2:
  print('Los números son iguales y ese número es: {}'.format(num1))

elif num1 < num2:
  print(f'El número {num2} es mayor al número {num1}')

else:
  print('El número ',num1,' es mayor al número ',num2)
 """
#EJERCICIO:
"""CREAR UN PROGRAMA QUE PIDA AL USUARIO SU NOMBRE Y SU EDAD.
LAS CONDICIONES SON:
1. SI LA PERSONA ES MENOR A 18 AÑOS, DEBE SOLICITARLE SU CARNE CON 1 DOSIS.
2. SI LA PERSONA TIENE ENTRE 18 Y 60 AÑOS, DEBE SOLICITARLE SU CARNE CON 2 DOSIS.
3. SI LA PERSONA TIENE SU EDAD MAYOR A LOS 60 AÑOS, DEBE SOLICITARLE SU CARNE CON LAS 3 DOSIS.
"""
print('Bienvenido al programa de solicitud de carné de vacunación')
#Insertar valores
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
edad = int(edad)

#verificar edad
if edad >=5 and edad < 18:
  print('Por favor, presente su carné con 1 DOSIS')
elif edad >= 18 and edad <= 60:
  print('Por favor, presente su carné con 2 DOSIS')
elif edad > 60 and edad <= 120:
  print('Por favor, presente su carné con 3 DOSIS')
else:
  print('Por favor colocar un número válido')


    



  
  