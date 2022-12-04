#Esta función realiza la comparación de dos números para ver si son diferentes o iguales
def is_different(num1: int, num2: int) -> bool:
  return True if num1 != num2 else False

my_num1 = float(input('Ingresa un primer número:'))
my_num2 = float(input('Ingresa un segundo número:'))

result = is_different(my_num1, my_num2)

print(result)
print(type(result))


