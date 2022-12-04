def mi_funcion():
  print('inicio de la función')
  return
  print('Esto no se muestra')

mi_funcion()

def sum_media(a, b, c):
  suma  = a + b + c
  media = suma / 3
  return suma, media

suma, media = sum_media(5,10,15)
print (suma)
print (media)

help ()
print(sum_media.__doc__)