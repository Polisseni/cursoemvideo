from modex109 import moeda109

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f'O dobro de R${moeda109.moeda(p)} é igual a R${moeda109.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda109.aumentar(p,10, True)}')
print(f'Reduzindo 13% temos R${moeda109.diminuir(p,13, True)}')

#MÓDULO ABAIXO: CRIAR DIRETÓRIO NOVO (MODEX109) E UM PYTHON FILE (MOEDA109)
'''def metade (p = 0, format = False):
    res = p * 1/2
    return res if format is False else moeda(res)


def dobro (p = 0, format = False):
    res = p * 2
    return res if format is False else moeda(res)


def aumentar (p = 0, taxa = 0, format = False):
    res = p + (p * taxa/100)
    return res if format is False else moeda(res)


def diminuir (p = 0, taxa = 0, format = False):
    res = p - (p * taxa/100)
    return res if format is False else moeda(res)


def moeda (preço = 0, moeda ='R$', format = False):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
'''
