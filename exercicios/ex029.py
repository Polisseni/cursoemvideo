velocidade = float(input('Informe a velocidade do veiculo: '))
if velocidade >80:
    print(f'VOCÊ FOI MULTADO!! Sua velocidade de {velocidade:} ultrapassou o limite da via de 80km/h')
    multa = (velocidade - 80)*7
    print(f'O total a pagar de multa será de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')