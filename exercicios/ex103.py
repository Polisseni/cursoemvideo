def ficha (jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato')


#PROGRAMA PRINCIPAL
n = str(input('Nome do JOGADOR: ')).strip()
g = str(input('Número de GOLS: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
