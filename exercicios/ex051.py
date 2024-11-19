primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimotermo= primeiro + (10 - 1) * razão
for c in range (primeiro, décimotermo + razão, razão):
    print(f'{c}', end='>>>')
print('ACABOU')