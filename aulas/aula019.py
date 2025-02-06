pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': '38'}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos de idade')  #COMO JÁ ESTÁ DENTRO DE ASPAS SIMPLES, UTILIZAM-SE ASPAS DUPLAS
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
del pessoas['Sexo']  #PARA DELETAR UM ITEM DO DICIONÁRIO
pessoas['Nome'] = 'Leandro'  #PARA TROCAR O NOME DO USUÁRIO
pessoas['Peso'] = '98KG'  #PARA ADICIONAR UM ITEM AO DICIONÁRIO
for k in pessoas.keys(): #PARA CADA CHAVE EM PESSOAS:
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
#----------------------------------------------------------------------------------------------------------

#DICIONÁRIO DENTRO DE UMA LISTA:

brasil = list()
estado = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[0])  #PRIMEIRO ESTADO ADICIONADO
print(brasil[1])  #SEGUNDO ESTADO ADICIONADO
print(brasil[0]['UF'])
print(brasil[1]['Sigla'])
print()

#----------------------------------------------------------------------------------------------------------

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  #.copy() PARA COPIAR OS DICIONARIOS NAS LISTAS
print(brasil)
#  ESSE PRIMEIRO LAÇO FOI PARA A LISTA
for e in brasil:
    for v in e.values():
        print(v, end=' ')
print()
#  ESSE SEGUNDO LAÇO FOI PARA O DICIONÁRIO