''' PROBLEMA N°2:
Escribir un programa que lea un entero positivo 𝑛
introducido por el usuario y después muestre en pantalla
la suma de todos los enteros desde 1 hasta 𝑛.
La suma de los primeros 𝑛 enteros positivos
puede ser calculada de la siguiente forma:
      Suma = n(n+1)/2
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
n = int(input("¿Por favor, ingrese un número entero positivo?\n"))
Suma = n*(n+1)/2
Suma = int(Suma)
# SALIDA
print(f"La suma de todos los enteros positivos desde 1 hasta {n} es de: {Suma}")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
