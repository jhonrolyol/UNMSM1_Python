print("============================================")
print("=========== BIENVENIDO AL PROGRAMA =========")
print("============================================")

def Factorial(Numero):
    '''Esta función calcula el factorial
    de un número entero positivo'''
    if Numero <= 1:
        return 1
    else:
        return (Numero * Factorial((Numero - 1)))
print(f"El factorial de {5} es {Factorial(5)}")

print("============== FIN DEL PROGRAMA =============")
