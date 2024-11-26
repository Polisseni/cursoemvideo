'''from math import factorial
n = int(input('Digite um número pra saber seu factorial: '))
f = factorial(n)
print(f'O factorial de {n} é {f}.')'''

n = int(input('Digite um número qualquer para saber se FACTORIAL: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print(f'{f}')