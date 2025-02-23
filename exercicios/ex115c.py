from time import sleep


def leiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de DADOS interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;34m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    return opc


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do ARQUIVO!')
    else:
        print(f'Arquivo {nome} criado com SUCESSO!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! Ao ler o Arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os DADOS')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()


#PROGRAMA PRINCIPAL
arq = 'Curso Em Vídeo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        #OPÇÃO DE LISTAR O CONTEÚDO DE UM ARQUIVO
        lerArquivo(arq)
    elif resposta == 2:
        #OPÇÃO DE CADASTRAR UMA NOVA PESSOA
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #OPÇÃO DE SAIR DO SISTEMA
        cabeçalho('Saindo do Sistema... Muito Obrigado!')
        break
    else:
        #DIGITOU A OPÇÃO ERRADA NO MENU
        print('\033[1;31mERRO! Digite uma opção VÁLIDA!\033[m')
    sleep(2)
