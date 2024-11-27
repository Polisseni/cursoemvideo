print('-=' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 15)

n = int(input('Digite quantos termos vc quer mostrar: '))
t1 = 0
t2 = 1
print('~' * 20)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')