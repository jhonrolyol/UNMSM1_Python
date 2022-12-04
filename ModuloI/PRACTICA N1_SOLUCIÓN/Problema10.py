'''PROBLEMA N°10:
Ecuación de primer grado. Diseñar un programa para resolver
cualquier ecuación de primer grado de la forma: a * x + b = c.
El programa tendrá que pedir los valores de a, b y c, para
luego calcular el valor de x = (c - b) / a .Pero, si a = 0,
el programa dará un error, pues se produce una división
entre 0. Hay que evitar que, en la medida de lo posible,
el programa se pare por un error.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
a = float(input("¿Por favor, ingrese el valor de 'a'?\n"))
b = float(input("¿Por favor, ingrese el valor de 'b'?\n"))
c = float(input("¿Por favor, ingrese el valor de 'c'?\n"))
# SALIDA
if (a == 0):
    print(f"La ecuación de primer grado no tiene solución.")
else:
    x = (c - b) / a
    print(f"La solución de la ecuación de primer grado es: {x}")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")



