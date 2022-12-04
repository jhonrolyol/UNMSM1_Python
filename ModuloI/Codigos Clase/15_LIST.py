lista = [1, 2, 3, 4]
print(lista)

lista = list("1234")
print(lista)

lista = [1, "Juan", 3.1415,[1, 2]]
#Ubicar un elemento de la lista con indice
print(lista[1])
#print(lista[2])
#print(lista[-2])
#print(lista)
#borrar un elemento de la lista con indice
del lista[1]
print(lista)
print(lista[1])
print(lista[2][0])

lista2 = [1, 2, 3, 4, 5, 6]
print(lista2[0:2])
print(lista2[2:4])

lista2[0:4] = [10, 20, 30, 40]
print(lista2)