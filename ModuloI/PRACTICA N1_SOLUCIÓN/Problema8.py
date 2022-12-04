'''PROBLEMA N°8:
Diseñar un programa que, dado un número entero, muestre
por pantalla el mensaje "El número es par" cuando el número
sea par y el mensaje "El número es impar" cuando sea impar.
También debe preguntar si se desea seguir trabajando con más
números. (Recuerda que un número es par cuando el resto de
dividirlo entre 2 sea 0 y, en caso contrario, será impar).
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

'''
# ENTRADA
NumEntero = int(input("¿Por favor, ingrese un número entero?\n"))
# SALIDA
if (NumEntero%2 == 0):
    print(f"El número {NumEntero} es par")
else:
    print(f"El número {NumEntero} es impar")
print("¿Desea seguir trabajando con más números?") 
'''

Consulta = 'SÍ'
while Consulta == 'SÍ':
    Numero = int(input("Ingrese un número a consultar: "))
    if (Numero % 2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
    print("Digite 'SÍ' para continuar o 'NO' para terminar el proceso.")
    Consulta = input("¿Desea seguir consultando?\n").upper()
print("Se terminó el proceso")



print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")