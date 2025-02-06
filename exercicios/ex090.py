dados = dict()
result = list()
dados['Nome'] = str(input('Nome do Aluno: '))
dados['Média'] = float(input(f'Média do(a) {dados["Nome"]}: '))
result.append(dados.copy())
if dados['Média'] >= 7:
    dados['Situação'] = '\033[1;34mO aluno foi APROVADO!!\033[m'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = '\033[1;33mO aluno está em RECUPERAÇÃO!!\033[m'
else:
    dados['Situação'] = '\033[1;31mO aluno foi REPROVADO!!\033[m'
for k, v in dados.items():
    print(f'{k} = {v}')
