from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar num número entre 0 e 5, tente adivinha!!')
print('-=-'*20)
jogador = int(input('Em qual número estou pensando? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador==computador:
    print('PARABÉNS!! Você conseguiu adivinhar o que pensei!!')
else:
    print(f'ERRADO!! Eu pensei no número {computador} e não no número {jogador}')


