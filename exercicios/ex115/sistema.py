from ex115.cadastro import cadastrar__init__
from ex115.menu import menu__init__
from time import sleep

arq = 'D:\Aprendendo Python3\ex115\cadastro.txt'

if not cadastrar__init__.arquivoExiste(arq):
    cadastrar__init__.criarArquivo(arq)
while True:
    op = menu__init__.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Menu'])
    if op == 1:
        cadastrar__init__.lerArquivo(arq)
        sleep(2)
    elif op == 2:
        menu__init__.cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar__init__.addpessoa(arq,nome,idade)
    elif op == 3:
        menu__init__.cabecalho("\033[34mFINALIZANDO O MENU, OBRIGADO POR PARTICIPAR!\033[m")
        break
    else:
        print("\033[31mERRO, POR FAVOR DIGITE UM VALOR VÁLIDO!\033[m")
