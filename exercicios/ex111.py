from modex111.utilidadesCeV import moeda

preço = float(input('Digite o preço: R$ '))
moeda.resumo(preço, 22, 12)

#CRIAR PYTHON PACKAGE COM O NOME "UTILIDADESCEV" +2 PYTHON PACKAGE (DADOS, MOEDA) E COLAR OS MÓDULOS EM "MOEDA"
'''def metade (preço = 0, format = False):
    res = preço * 1/2
    return res if format is False else moeda(res)


def dobro (preço = 0, format = False):
    res = preço * 2
    return res if format is False else moeda(res)


def aumentar (preço = 0, taxa = 0, format = False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)


def diminuir (preço = 0, taxa = 0, format = False):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)


def moeda (preço = 0, moeda ='R$', format = False):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo (preço = 0, taxaa = 10, taxad = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(preço, taxad, True)}')
    print('-' * 30)'''
