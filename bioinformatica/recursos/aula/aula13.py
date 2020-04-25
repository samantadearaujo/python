#c = {1, 2, 2, 3, 4}
#c.add(3)
#print(c)

'''
lista = [1,2,3,4,4,5,5,5,10]

if 5 in lista:
	print('pertence a lista')
else:
	print('nao pertence a lista')

c = set(lista)
print(c)

if 100 in c:
	print('pertence ao conjunto')
else:
	print('nao pertence ao conjunto')
'''

c1 = {1,2,3,4,5}
c2 = {4,5,6}
uniao = c1 | c2
inter = c1 & c2
print(uniao)
print(inter)