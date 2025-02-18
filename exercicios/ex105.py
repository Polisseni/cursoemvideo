def notas (*n, sit=False):
    """
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


#PROGRAMA PRINCIPAL
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
