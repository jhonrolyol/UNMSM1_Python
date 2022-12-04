'''PROBLEMA N°9:
Escribir un programa que solicite un número
de segundos y muestre por pantalla dicha cantidad
de tiempo en horas, minutos y segundos.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
NumSegundos = int(input("¿Por favor, ingrese un número determinado de segundos?\n"))
Horas = NumSegundos/3600
Horas = int(Horas)
Minutos = Horas*60
Minutos = int(Minutos)
Segundos = Minutos*60
Segundos = int(Segundos)
# SALIDA
print(f"El tiempo en horas es: {Horas} horas")
print(f"El tiempo en minutos es: {Minutos} minutos")
print(f"El tiempo en segundos es: {Segundos} segundos")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
