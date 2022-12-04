"""vidas = input('¿Cuántas vidas desea tener?')
#vidas = int(vidas)
print(vidas)
vidas = vidas - 1
print(vidas)
#print(type(vidas))

vidas -= 1
print(vidas)

#EJERCICIO:
HACER UN PROGRAMA QUE INSERTE VALORES DE PRESUPUESTOS DE LOS 3 PRIMEROS MESES DEL AÑO (CADA MES) Y CALCULAR EL PROMEDIO DE ELLOS: UTILIZAR VARIABLES Y OPERACIONES.

mes_1 =float(input('¿Ingrese importe para el mes de Enero?'))
mes_2 =float(input('¿Ingrese importe para el mes de Febrero?'))
mes_3 =float(input('¿Ingrese importe para el mes de Marzo?'))
promedio=(mes_1+mes_2+mes_3)/3
resultado=f"El promedio de ventas de Enero, Febrero y Marzo es: {promedio}"
print(resultado)
"""
Ene = float(input('¿ingresar el presupuesto de enero?'))
Feb = float(input('¿ingresar el presupuesto de febrero?'))
Mar = float(input('¿ingresar el presupuesto de Marzo?'))

suma = (Ene + Feb + Mar)
print(suma)
promedio = format((suma/3),"2g")
#promedio = suma/3
print(promedio)