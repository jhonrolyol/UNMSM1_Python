print("============================================")
print("=========== BIENVENIDO AL PROGRAMA =========")
print("============================================")

Pregunta = "SI"
while Pregunta == "SI":
    n = int(input("¿Por favor, ingrese un número entero?\n"))
    if n%2 == 0:
        print(f"El número {n} es par")
    else:
        print(f"El número {n} es impar")
    Pregunta = input("¿Desea seguir trabajando con más números?\n").upper()

print("Estimado usuario se terminó el proceso")

print("============== FIN DEL PROGRAMA =============")
