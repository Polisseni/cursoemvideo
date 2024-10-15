dias=int(input('Informe a quantidade de dias que permaneceu com o veículo alugado: '))
km=float(input('Informe a kilometragem rodada com o veículo: '))
pagar=(dias*60)+(km*0.15)
print(f'Valor a pagar: R${pagar:.2f}')
