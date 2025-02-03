num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if res in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
num.sort()
print(f'A lista completa é {num}')
num.sort()
print(f'A lista dos valores pares é {pares}')
num.sort()
print(f'A lista dos valores ímpares é {impares}')
