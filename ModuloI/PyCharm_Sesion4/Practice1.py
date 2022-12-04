
print("============= DATOS DE ENTRADA ==================")
Nombre = input("¿Ingrese su nombre?\n")
Apellido = input("¿Ingrese su apellido?\n")
Edad = int(input("¿Ingrese su edad?\n"))

print("================= PROGRAMA =======================")
if (Edad < 18):
    print(f"Estimado(a) {Nombre}, usted es menor de edad")
elif (Edad >= 18) and (Edad < 41):
    print(f"Estimado(a) {Nombre}, usted es un joven")
elif (Edad >= 41) and (Edad <= 65):
    print(f"Estimado(a) {Nombre}, usted es un adulto")
else:
    print(f"Estimado(a) {Nombre}, usted es un adulto mayor")
