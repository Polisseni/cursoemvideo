nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Prazer em te conhecer, {nome}!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')

