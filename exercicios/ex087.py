matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = somacol = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite uma valor para [{l}, {c}]: '))
print('-='*30)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'{matriz[l][c]:^5}', end='')  #:^5 = 5 ESPAÇOS CENTRALIZADO
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {somapar}')
for l in range (0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for c in range (0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
