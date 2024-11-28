resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
media = soma / quant
print(f'Você digitou {quant} valores e a soma deles foi de {soma}')
print(f'O maior valor entre eles foi {maior} e o menor foi {menor}')

