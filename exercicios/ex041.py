from datetime import date
ano = int(input('Digite o ANO DE NASCIMENTO: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos e sua categoria será a de:')
if 9 >= idade:
    print('ATLETA MIRIM')
elif idade <= 14:
    print('ATLETA INTANTIL')
elif idade <= 19:
    print('ATLETA JÚNIOR')
elif idade <= 25:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')
