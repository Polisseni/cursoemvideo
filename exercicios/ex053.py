frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS UM POLÍNDROMO')
else:
    print('NÃO É UM POLÍNDROMO')

