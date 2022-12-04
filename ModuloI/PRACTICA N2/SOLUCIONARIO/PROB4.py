#PROBLEMA 4
#Realizar un programa que solicite a un usuario ingresar un número entero e informar si es primo o no, utilizando una función booleana que tome la decisión.
"""
La función siguiente recibirá como dato un número entero el cual será como referencia para poder crear una lista de números desde el 2 hasta el número, luego se procederá a buscar si en alguna de sus divisiones el resto sale 0, de ser así entonces se sabrá que dicho número no es primo, de lo contrario lo será
"""
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

print('******VERIFICADOR DE NÚMERO PRIMO ******') 
numero=int(input("Ingrese un número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")
