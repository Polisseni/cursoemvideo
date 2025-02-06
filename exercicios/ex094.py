galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('\033[1;31mERRO! DIGITE APENAS "M" OU "F"\033[m')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']  #SOMA + IDADE DA PESSOA
    galera.append(pessoa.copy())
    while True:
        resp = str(input('QUER CONTINUAR?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31mERRO! DIGITE APENAS "S" OU "N"\033[m')
    if resp in 'N':
        break
print('-='*30)
print(f'Ao todo, {len(pessoa)} pessoas foram cadastradas')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'A(s) mulher(es) cadastrada(s) foi(ram): ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f'Lista das pessoas que estão acima da média: ')
for p in galera:
    if p["Idade"] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}')
        print()
print('<<ENCERRADO>>')
