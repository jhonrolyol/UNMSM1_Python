''' PROBLEMA N° 5
Realice un programa que tenga una función “ConvertirEspaciado”,
que reciba como parámetro un texto y devuelva una cadena
con un espacio adicional en cada letra.
Ejemplo:
Ingresamos: “Hello World”.
Devolverá: “H e l l o W o r l d”.
'''
print("=============================================")
print("===========  BIENVENIDO AL PROGRAMA =========")
print("=============================================")

def ConvertirEspaciado(Texto):
    '''
    Esta función recibe un texto y lo devuelve con un
    espaciado adicional en cada letra.
    '''
    Pregunta = input("¿Por favor,ingrese un texto?\n")
    print(" ".join(Pregunta))
    return Pregunta
ConvertirEspaciado("Hello World")

print("=============================================")
print("============== FINAL DEL PROGRAMA ===========")
print("=============================================")
