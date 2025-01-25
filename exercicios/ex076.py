listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 12.50,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.99,
            'Canetas', 22.30,
            'Livro', 60.00)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')

