from random import randint

computador = randint (0, 10)
print('\033[1;34mSOU O SEUM COMPUTADOR... PENSEI NUM NÚMERO ENTRE 0 E 10\033[m')
print('\033[1;34mSERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL É...\033[m')
acertou = False
contador = 0
while not acertou:
    jogador = int(input('QUAL O SEU PALPITE?: '))
    contador += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador > computador:
            print('\033[1;34mMENOS...\033[m')
        elif jogador < computador:
            print('\033[1;34mMAIS...\033[m')
print(f'\033[1;36mPARABÉNS!!! VOCÊ ACERTOU COM {contador} TENTATIVAS!!!\033[m')
