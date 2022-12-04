''' PROBLEMA N° 1
Realizar un programa mediante una función que reciba
una muestra de números en una lista y devuelva su media.
'''
print("=============================================")
print("===========  BIENVENIDO AL PROGRAMA =========")
print("=============================================")

def MediaAritmetica(MuestraDeNumeros):
    """
    Esta función calcula la media aritmética
    de los números ingresados como una lista.
    """
    MA = sum(MuestraDeNumeros)/len(MuestraDeNumeros)
    return MA

print(f"La media aritmética es: {MediaAritmetica([2, 4, 6, 8, 10])}")

print("=============================================")
print("============== FINAL DEL PROGRAMA ===========")
print("=============================================")
