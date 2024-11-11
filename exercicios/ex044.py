print('{:=^40}'.format(' LOJAS POLISSENI '))
preço = float(input('Digite o preço das compras R$: '))
print('''ESCOLHA UMA DAS OPÇõES DE PAGAMENTO:
OPÇÃO [1] À VISTA NO DINHEIRO/CHEQUE
OPÇÃO [2] À VISTA NO CARTÃO
OPÇÃO [3] 2X NO CARTÃO
OPÇÃO[4] 3X OU MAIS NO CARTÃO''')
opção = int(input('Qual a forma de pagamento?'))
if opção == 1:
    total = preço - (preço * 10/100)
    print(f'O valor da compra com 10% de desconto será de R${total:.2f}')
elif opção == 2:
    total = preço - (preço * 5/100)
    print(f'O valor da compra com 5% de desconto é R${total:.2f}')
elif opção == 3:
    total = preço
    parcela = total/2
    print(f'Sua compra será parcelada em 2x de R${total:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas deseja pagar?: '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = preço
    print('\033[1:31mOPÇÃO INVÁLIDA DE PAGAMENTO, TENTE NOVAMENTE\033[m')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')
