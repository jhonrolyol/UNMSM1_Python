#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#n = 4
#fact: 0*1*2*3*4 = (n)(n-1)(n-2)....*1

def factorial(n):
  """
  Esta función calcula el factorial de un número entero positivo ingresado.
  Parámetros:
  n = entero positivo.
  Devolver: factorial de n
  """
  temp = 1
  for i in range(n): # n = 4 list(n) = [0,1,2,3]
    temp = temp*(i+1)
    #1   =  1  * (1)
    
  return temp

print('====FACTORIAL====')
x = int(input('Ingrese un número entero positivo: '))
print('El factorial del numero ',x,'es ',factorial(x))