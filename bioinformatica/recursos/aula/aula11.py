'''
O que é tuplas?
Tuplas podem ser consideradas similares às listas, mas suas diferenças são cruciais.
Quanto à sintaxe, a tupla se diferencia por substituir os colchetes ([]) das listas por parênteses (()):
Isso significa que não podemos alterar um mesmo objeto tupla, ou seja, mudar uma de suas referências internas (seus valores), 
nem adicionar ou remover elemento algum
-----------------------------------------------------------------------------------------------------------------------------
Listas e tuplas são algumas estruturas de dados muito utilizadas quando estamos programando. 
Essas duas estruturas nos permitem guardar nossos dados agrupados, contudo suas semelhanças se encerram por aí, como pudemos ver nesse post.
Conseguimos desmistificar a ideia de que a tupla é apenas uma lista imutável, e entendemos como as listas têm uma função semântica diferente das tuplas.
'''

tupla = (1, 2, 3, 4)

lista = list(tupla)

print(lista)

lista.append(10)

tupla = tuple(lista)

print(tupla)