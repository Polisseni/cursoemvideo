print('\033[1;34mOS NÚMEROS PARES ENTRE 1 E 50 SÃO:\033[m')
for c in range (2, 51, 2):
    print(c)
print('FIM')


for c in range (1, 51):
    print('.', end=' ')
    if c % 2 ==0:
        print(c, end=' ')
print('FIM')