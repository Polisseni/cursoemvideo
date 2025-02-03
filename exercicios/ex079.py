numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado NÃO adicionado!!')
    r = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if r in 'Nn':
        break
print('=-'*30)
numeros.sort()   #SÓ ISSO JÁ COLOCA EM ORDEM
print(f'Você digitou os valores: {numeros}')
