from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint (0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, num total de {total}')
    print('DEU PAR!!' if total % 2 == 0 else 'DEU ÍMPAR!!')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;34mVOCÊ VENCEU!!\033[m')
            v += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;34mVOCÊ VENCEU!!\033[m')
            v += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!!\033[m')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'GAME OVER!! Você venceu {v} vezes consecutivas')
