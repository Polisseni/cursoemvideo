nome = str(input('Digite seu nome completo: ')).strip() #removendo os espaços antes e depois do nome
print('Analisando seu nome...')
print(f'Seu nome em letras maiusculas é: {nome.upper()}')
print(f'Seu nome em letras minusculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {(len(nome)-nome.count(' '))} letras') #removando os epaços entre os nomes
#print(f'Seu primeiro nome tem ao todo {nome.find(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem ao todo {len(separa[0])} letras')
