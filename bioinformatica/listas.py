lista = [32,'Samanta', 4.000]

print(lista)
print(len(lista))

for e in range(len(lista)):
    print(lista[e])


lista1 = [1,2,3,4,5,6]

lista1.append(7)

print(lista1)

lista2 = lista +lista1

print(lista2)


lista3 = [1,2,3,4,5,6,7,8]

removido = lista3.pop(0)
print(removido)


lista4= [1,2,3,4,5,6,7,8,9]
lista4.remove(3)
print(lista4)

print(lista4[::-1])

print(lista4[0::-1])

lista4.insert(3,100)
print(lista4)

lista5 = [50,37,89,1,2,3,70]
lista5.sort()

print(lista5)

