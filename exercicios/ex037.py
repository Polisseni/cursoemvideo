num = int(input('Digite um número inteiro: '))
print('''ESCOLHA UMA DAS OPÇOES A SEGUIR:
[1] PARA BINÁRIO
[2] PARA OCTAL
[3] PARA HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print(f'A conversão para BINÁRIO de {num} é {bin(num)[2:]}')
elif opção == 2:
    print(f'A conversão de {num} para OCTAL é {oct(num)[2:]}')
elif opção == 3:
    print(f'A conversão de {num} para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção INVÁLIDA, tente novamente')


