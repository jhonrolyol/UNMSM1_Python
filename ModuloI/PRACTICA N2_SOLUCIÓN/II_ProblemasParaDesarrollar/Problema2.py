''' PROBLEMA N° 2
Realizar un programa mediante una función que solicite
al usuario que ingrese su dirección email. Imprimir
un mensaje indicando si la dirección es válida o no,
valiéndose de una función para decidirlo. Una dirección
se considerará válida si contiene el símbolo "@".
'''

print("=============================================")
print("===========  BIENVENIDO AL PROGRAMA =========")
print("=============================================")


def Usuario(CorreoElectronico):
    '''
    Esta función solicita al usuario que ingrese 
    su correo electrónico.
    '''
    Arroba = "@"
    ValidesDelCorreoElectronico = False
    for i in CorreoElectronico:
        if i == Arroba:
            return True
    return False

Correo = input("Por favor, ingrese su correo electrónico: ")
if Usuario(Correo):
    print("El correo es válido")
else:
    print("El correo no es válido")


print("=============================================")
print("============== FINAL DEL PROGRAMA ===========")
print("=============================================")
