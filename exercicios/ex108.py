from modex108 import moeda108

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda108.moeda(p)} é {moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de R${moeda108.moeda(p)} é igual a R${moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda108.moeda(moeda108.aumentar(p,10))}')
print(f'Reduzindo 13% temos R${moeda108.moeda(moeda108.diminuir(p,13))}')

#MÓDULO ABAIXO: CRIAR DIRETÓRIO NOVO (MODEX108) E UM PYTHON FILE (MOEDA108)
'''def metade (p = 0):
    res = p * 1/2
    return res


def dobro (p = 0):
    res = p * 2
    return res


def aumentar (p = 0, taxa = 0):
    res = p + (p * taxa/100)
    return res


def diminuir (p = 0, taxa = 0):
    res = p - (p * taxa/100)
    return res


def moeda (preço = 0, moeda ='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')
#>8.2f ALINHADO A DIREITA, 2 ÚLTIMAS COMO .00 (EX:100.00)
'''
