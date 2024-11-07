distância = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a iniciar uma viagem de {distância:.2f} kms')
#preço = distância * 0.50 if distância <=200 else distância * 0.45
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'O preço da passagem será de R${preço:.2f}')
