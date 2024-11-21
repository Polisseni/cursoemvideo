num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
opçao = 0
while opçao != 5:
    print('ESCOLHA A SUA OPÇÃO:\
    \nOPÇÃO [1] SOMAR\
    \nOPÇÃO [2] MULTIPLICAR\
    \nOPÇÃO [3] MAIOR\
    \nOPÇÃO [4] NOVOS NÚMEROS\
    \nOPÇÃO [5] SAIR DO PROGRAMA')
    opçao = int(input('Digite a sua opção: '))
    if opçao == 1:
        soma = num1 + num2
        print(f'O valor da soma entre {num1} e {num2} é {soma}')
    elif opçao == 2:
        produto = num1 * num2
        print(f'O valor do produto entre {num1} e {num2} é {produto}')
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior valor entre os dois é {maior}')
    elif opçao == 4:
        num1 = float(input('Digite o primeiro novo valor: '))
        num2 = float(input('Digite o segundo novo valor: '))
    elif opçao == 5:
        print('\033[1;35mFINALIZANDO...\033[m')
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
    print('-*-*-*-*-*-*' * 5)
print('FIM DO PROGRAMA, VOLTE SEMPRE!!!')
