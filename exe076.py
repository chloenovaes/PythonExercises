print('{:->31}'.format('-'))
print('{:^33}'.format('LISTAGEM DE PREÇOS'))
print('{:->31}'.format('-'))
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for itens in listagem:
    if type(itens) == str:
        print('{:.<24}{}'.format(itens,'R$'), end=' ')
    else:
        print('{:.2f}'.format(itens))
print('{:->31}'.format('-'))
