from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    dados['Aposenatodria'] = ((dados['Ano de Contratação'] + 35) - datetime.now().year)
print('-='*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')
