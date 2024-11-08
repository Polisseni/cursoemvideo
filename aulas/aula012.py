nome = str(input('Qual é o seu nome? '))
if nome == 'Vitor':
    print(f'Que belo nome você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é muito comum no Brasil')
elif nome in 'Ana Clara Carolina Juliana':
    print('Que belo nome feminino você tem!')
else:
    print(f'Nada de especial no seu nome, {nome}...')
print(f'Tenha um bom dia, {nome}!')