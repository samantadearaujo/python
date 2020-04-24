preco = 200

if preco > 100:
    print('Nao vou comprar o produto')
else:
    if preco < 50:
        print('Muito barato')


if preco > 100:
    print('Vou comprar o produto')
elif preco == 50:
    print('Preco Topo')
else:
    print('Todo certo')



if preco == 100:
    print('Vou pensar se compro o produto...')