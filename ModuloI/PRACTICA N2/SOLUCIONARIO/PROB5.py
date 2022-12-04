#PROBLEMA 5
#Realice un programa que tenga una función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelva una cadena con un espacio adicional en cada letra. Ejemplo: Ingresamos: “Hello World”. Devolverá: “H e l l o W o r l d”.
"""
Función Espaciado: Recibe una cadena de caracteres, y devuelve otra 
con los mismos caracteres separados con espacio.
Parámetros de entrada: Cadena de caracteres
Dato devuelto: Cadena igual a la anterior pero con espacios entre los caracteres
"""
print('****** CONVERTIR ESPACIADO ******')

def Espaciado(cadena):
	cadena_espacio = cadena.replace(""," ")
	return cadena_espacio

mensaje = input("Introduce una cadena:")
print("La cadena con espacio:", Espaciado(mensaje))
