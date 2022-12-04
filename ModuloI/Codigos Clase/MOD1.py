#Modulo o module ".py"
import operaciones

print(operaciones.suma(5,8))
print(operaciones.resta(9,4))

#USO DEL FROM IMPORT
from operaciones import suma, resta
print(resta(4,9))

#USO DEL IMPORT *
from operaciones import *
print(suma(5,8))
print(resta(9,4))

#RUTAS
archivo1.py
CARPETA
  archivo2.py

#archivo2.py:
def hola():
  print('hola')

#archivo1.py
from CARPETA.archivo2 import *
print(hola())