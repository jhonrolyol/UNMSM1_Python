''' PROBLEMA N° 4
Realizar un programa que solicite a un usuario ingresar
un número entero e informar si es primo o no, utilizando
una función booleana que tome la decisión.
'''
print("=============================================")
print("===========  BIENVENIDO AL PROGRAMA =========")
print("=============================================")
# Creamos la función
def NumeroPrimo(Z):
    '''
    Esta función sirve para identificar si un número entero
    positivo es primo o no.
    '''
    if Z == 1: # 1 no es primo
        return False
    elif Z == 2: # 2 si el primo
        return True
    else:
        for k in range(2,Z): # El rango inicia en 2, porque 2 es el primer número primo.
            if Z%k == 0:
                return False
        return True
# Llamamos a la función
for k in range(1,1001):
    print(f"¿El número {k} es primo?\n{NumeroPrimo(k)}")

print("=============================================")
print("============== FINAL DEL PROGRAMA ===========")
print("=============================================")
