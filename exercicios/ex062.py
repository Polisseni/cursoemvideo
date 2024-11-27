print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        cont += 1
    print('\033[0;31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Prograssão finalizada com {total} termos mostrados.')