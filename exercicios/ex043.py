peso = float(input('Digite seu peso(kg):'))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura**2)
print(f'Com o peso de {peso} kg e altura de {altura} m seu IMC de {imc:.1f} é considerado', end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25: #elif 18.5 >= imc <25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30: #elif 25 >= imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40: #elif 30 >= imc < 40:
    print('OBESIDADE')
#elif imc >= 40:
else:
    print('OBESIDADE MÓRBIDA')


