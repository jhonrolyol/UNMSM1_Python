#PROBLEMA 2
#Realizar un programa mediante una función que solicite al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
"""
La siguiente función realizará la búsqueda del caracter "@" dentro de la cadena ingresada, si encuentra el caracter mencionado, indicará que la dirección de correo es VÁLIDA, de lo contrario indicará que es INVÁLIDA.
"""
print('****** VALIDACIÓN DE CORREO ELECTRÓNICO ******')

def validar(correo):
    caracterBuscado="@"
    for c in correo:
        if c==caracterBuscado:
            return True
    return False

direccion=input("Ingresa tu correo electrónico: ")
if validar(direccion):
    print("La dirección de correo ingresada es VÁLIDA")
else:
    print("La dirección de correo ingresada es INVÁLIDA")
