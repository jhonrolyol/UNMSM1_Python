'''PROBLEMA N°5:
Escribir un programa que pregunte por consola
por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla
cada uno de los productos en una línea distinta.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")
print("Por favor, a continuación responda las siguientes preguntas: ")
# ENTRADA
Producto1 = input("¿Cuál es el primer producto que compró?\n")
Producto2 = input("¿Cuál es el segundo producto que compró?\n")
Producto3 = input("¿Cuál es el tercer producto que compró?\n")
# SALIDA
print("A continuación se muestra los productos comprados: ")
for Cesta in [Producto1, Producto2, Producto3]:
    print(f"- {Cesta}")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
