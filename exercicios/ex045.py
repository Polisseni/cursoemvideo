from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint (0,2)
print('''ESCOLHA SUA OPÇÃO:
OPÇÃO [0]: PEDRA
OPÇÃO [1]: PAPEL
OPÇÃO [2]: TESOURA''')
jogador = int(input('Escolha sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('-=' * 15)
print(f'O COMPUTADOR ESCOLHEU {itens[computador]}')
print(f'O JOGADOR ESCOLHEU {itens[computador]}')
print('-=' * 15)
if computador == 0:          #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('\033[1;34mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU!!!\033[m')
    elif jogador ==2:
        print('\033[1;35mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
elif computador == 1:        #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('\033[1;35mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1;34mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCEU!!!\033[m')
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
elif computador == 2:        #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[1;35mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;34mEMPATE\033[m')
else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
