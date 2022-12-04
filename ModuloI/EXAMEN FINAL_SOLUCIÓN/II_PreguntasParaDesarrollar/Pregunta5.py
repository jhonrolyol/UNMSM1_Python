print("============================================")
print("=========== BIENVENIDO AL PROGRAMA =========")
print("============================================")

EscribirFrase = input("¿Por favor, escriba una frase?\n")
EscribirLetra = input("¿Por favor, escriba una letra?\n")
Veces = 0
# Usamos el bucle for:
for i in EscribirFrase:
    if i == EscribirLetra:
        Veces += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (EscribirLetra, Veces, EscribirFrase))


print("============== FIN DEL PROGRAMA =============")







