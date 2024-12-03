total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto:R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${total:.2f}')
print(f'{totmil} produtos se encontram a cima de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
