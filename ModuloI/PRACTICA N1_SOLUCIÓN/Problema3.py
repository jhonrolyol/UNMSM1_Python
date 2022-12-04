'''PROBLEMA N°3:
Escribir un programa que pida al usuario su peso (en kg)
y estatura (en metros), calcule el índice de masa corporal
y lo almacene en una variable, y muestre por pantalla
la frase Tu índice de masa corporal es <imc> donde <imc>
es el índice de masa corporal calculado redondeado con dos
decimales.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
Peso = float(input("¿Por favor, ingrese su peso (kg)?\n"))
Estatura = float(input("¿Por favor, ingrese su estatura (m)?\n"))
imc = Peso/Estatura**2
imc = int(imc)
# SALIDA
print(f"Tu índice de masa corporal es {imc}")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
