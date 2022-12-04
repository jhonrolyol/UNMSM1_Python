'''PROBLEMA N°6:
Para tributar un determinado impuesto se debe ser mayor
de 18 años y tener unos ingresos iguales o superiores a
2500 dólares mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
Nombre = input("¿Por favor, ingrese su nombre?\n")
Edad = int(input("¿Por favor, ingrese su edad?\n"))
Ingreso = int(input("¿Por favor, escriba la cantidad de sus ingresos mensuales en dólares?\n"))
# SALIDA
if (14 <= 18 < Edad) and (Ingreso >= 2500):
    print(f"{Nombre}, usted tiene que tributar.")
else:
    print(f"{Nombre}, usted no tiene que tributar.")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
