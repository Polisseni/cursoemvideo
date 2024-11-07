salário = float(input('Qual é o salário do funcionário? '))
if salário <= 1250.00:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print(f'O valor do novo salário com aumento será de R${novo:.2f}')