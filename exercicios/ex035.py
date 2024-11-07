print('-=-'*20)
print('ANALISADOR DE TRINÂNGULOS')
print('-=-'*20)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM formar um TRIÂNGULO')