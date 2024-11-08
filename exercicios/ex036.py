casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário do comprador? R$'))
hipoteca = int(input('Em quantos anos pretende pagar? '))
prestação = casa / (hipoteca * 12)
mínimo = salário * 30/100
print(f'Para pagar uma casa de R${casa:.3f} em {hipoteca} anos a prestação será de R${prestação:.3f}')
if prestação <= mínimo:
    print('SEU EMPRÉSTIMO FOI APROVADO!!')
else:
    print('SEU EMPRÉSTIMO FOI NEGADO!!!')