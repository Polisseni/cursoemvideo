sexo = str(input('INFORME SEU SEXO[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\033[1;31mINFORMAÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
    sexo = str(input('INFORME SEU SEXO[M/F]: ')).strip().upper()[0]
print(f'DADOS SALVOS, O INDIVÍDUO É DO SEXO {sexo}')
