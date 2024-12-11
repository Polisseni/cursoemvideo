cont = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE',
        'OITO','NOVE','DEZ','ONZE','DOZE','TREZA','CATORZE',
        'QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:  #SE O NÚMERO ESTIVER ENTRE ZERO E VINTE:
        break
    print('\033[1;31mTENTE NOVAMENTE\033[m')
print(f'Você digitou o número {cont[num]}')