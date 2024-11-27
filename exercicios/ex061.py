print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    cont += 1
print('\033[0;31mFIM\033[m')
