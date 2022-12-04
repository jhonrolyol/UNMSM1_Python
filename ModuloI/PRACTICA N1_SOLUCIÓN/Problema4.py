'''PROBLEMA N°4:
Imagina que acabas de abrir una nueva cuenta de ahorros
que te ofrece el 5% de interés al año. Estos ahorros debido
a intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la cuenta
de ahorros, introducida por el usuario. Después el programa debe calcular
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y
tercer años. Redondear cada cantidad a dos decimales.
'''
print("================================================")
print("========= BIENVENIDO AL PROGRAMA ===============")
print("================================================")

# ENTRADA
Deposito = int(input("¿Por favor, ingrese la cantidad de dinero a depositar?\n"))
FirstYear = round(float(Deposito*1.05), 2)
SecondYear = round(float(FirstYear*1.05), 2)
ThirdYear = round(float(SecondYear*1.05), 2)
# SALIDA
print(f"La cantidad de dinero depositado es: S/{Deposito}")
print(f"El monto tras el primer año será : S/{FirstYear}")
print(f"El monto tras el segundo año será : S/{SecondYear}")
print(f"El monto tras el tercer año será : S/{ThirdYear}")

print("================================================")
print("=============== FIN DEL PROGRAMA ===============")
print("================================================")
