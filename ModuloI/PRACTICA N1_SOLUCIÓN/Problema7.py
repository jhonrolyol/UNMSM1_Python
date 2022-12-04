'''PROBLEMA N°7:
Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la
contraseña hasta que introduzca la contraseña correcta.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
Variable = str("contraseña")
Pregunta = " "
# SALIDA
while (Pregunta != Variable):
    Pregunta = str(input("Por favor, introdusca la contraseña: "))
print("Felicitaciones, acertaste la contraseña")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
