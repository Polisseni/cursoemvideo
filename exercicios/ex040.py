nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f} a média é: {média:.1f}')
if média > 7:
    print('O aluno está \033[4:34mAPROVADO\033[m!! \033[0:34mPARABÉNS\033[m!!!')
elif 7 > média >= 5:
#if média >= 5 and média < 7:
    print('O aluno está em \033[4:33mRECUPERAÇÃO\033[m')
else:
    print('O aluno foi \033[4:31mREPROVADO\033[m')

