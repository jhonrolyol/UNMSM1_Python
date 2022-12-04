print("======================================")
print("======= BIENVENIDO AL PROGRAMA =======")
print("======================================")

#%% DATOS DE ENTRADA
Minimo = int(input("¿Ingrese el valor mínimo?\n"))
Maximo = int(input("¿Ingrese el valor máximo?\n"))
Divisor = int(input("¿Ingrese el divisor?\n"))

#%% DATOS DE SALIDA
while (Minimo <= Maximo):
    if (Minimo % Divisor == 0): 
        print(f"El número {Minimo} es divisible por 7")
    Minimo += 1

