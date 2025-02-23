try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[1;31mTivemos um problema com o tipo de dados que você digitou :(\033[m')   #DIGITAR POR EXTENSO, DEIXAR VAZIO SEM RESPOSTA...
except ZeroDivisionError:
    print('\033[1;31mImpossível divisão por ZERO!!\033[m')
except KeyboardInterrupt:
    print('\033[1;31mO usuário preferiu não informar os DADOS!\033[m')  #INTERROMPENDO O RUN
except Exception as error:
    print(f'\033[1;33mO erro encontrado foi {error.__cause__}\033[m')   #ERRO GENÉRICO
else:
    print(f'A resposta de {a} dividido por {b} é igual a {r:.2f}!')
finally:
    print('\033[1;36mVOLTE SEMPRE!! MUITO OBRIGADO :)\033[m')
