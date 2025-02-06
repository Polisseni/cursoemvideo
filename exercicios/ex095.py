time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('QUER CONTINUAR?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31mERRO! DIGITE APENAS "S" OU "N"\033[m')
    if resp == 'N':
        break
print('-='*30)
print('Cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 PARA ENCERRAR]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[1;31mERRO! NÃO EXISTE NENHUM JOGADOR COM O CÓDIGO {busca}\033[m')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i,g in enumerate (time[busca]["Gols"]):
            print(f'  No jogo {i+1} fez {g} gols')
        print('-='*30)
print('<<<VOLTE SEMPRE>>>')
