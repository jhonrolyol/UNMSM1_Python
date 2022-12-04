''' PROBLEMA N°6 : Ejercicio Extra
Crear un programa principal donde se pida un nombre de usuario
y una contraseña y se intente hacer login, solamente tenemos
tres oportunidades para intentarlo.
Para la función llamada “Login”, este recibirá un nombre de usuario
y una contraseña y devolverá Verdadero si el nombre de usuario
es (ejemplo: “usuario1” y la contraseña es “asdasd”). Además,
recibe el número de intentos que se ha intentado hacer login
y si no se ha podido hacer login incremente este valor.
'''
print("=============================================")
print("===========  BIENVENIDO AL PROGRAMA =========")
print("=============================================")

def  Login():
    '''
    Esta función pide un nombre de usuario
    y una contraseña e intentar hacer login.
    '''
    Nombre = input("¿Por favor, ingrese su nombre?\n")
    Contraseña = input("¿Por favor, ingrese su contraseña?\n")
    if Nombre == 'Lucas' and Contraseña == '12345':
        print("True")
    else:
        print("False")
Login()

print("=============================================")
print("============== FINAL DEL PROGRAMA ===========")
print("=============================================")
