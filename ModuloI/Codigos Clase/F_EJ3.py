#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#MCD
#MCM

def mcd(a, b):
  """
  Esta función calcula el máximo común divisor de dos números,
  Parámetros:
  a y b: num enteros.
  Devolver:
  El mcd de a y b
  """
  resto = 0
  while (b > 0):
    resto = b # 21 #9 #3
    b = a % b #  9 #3 #0
    a = resto # 21 #9 #3
  return a

def mcm(a, b):
  """
  Esta función calcula el minimo comun multiplo de dos numeros.
  parámetros: a y b: numeros enteros
  devuelve: el mcm de a y b
  """
  if a > b:
    mayor = a
  else:
    mayor = b
  
  while (mayor % a != 0) or (mayor % b !=0):
    mayor = mayor + 1
  return mayor

print ('====MCD Y MCM====')
x = int(input('Ingrese un primer número: '))
y = int(input('Ingrese un segundo número: '))
print ('El MCD de ',x,'y',y,'es',mcd(x,y))
print ('El MCM de ',x,'y',y,'es',mcm(x,y))