from modex112.utilidadesCeV import moeda
from modex112.utilidadesCeV import dados

preço = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preço, 22, 12)

#CRIAR PYTHON PACKAGE COM O NOME "UTILIDADESCEV" +2 PYTHON PACKAGE (DADOS, MOEDA) E COLAR OS MÓDULOS EM "DADOS"
'''def leiaDinheiro (msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()  #SUBSTITUINDO TODAS AS VIRGULAS POR PONTOS
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: \'{entrada}\' é um preço INVÁLIDO\033[m')
        else:
            valido = True
            return float(entrada)
        '''
