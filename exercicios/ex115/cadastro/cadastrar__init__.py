from ex115.menu import menu__init__
def arquivoExiste(nome):
    try:
        with open(nome,'rt') as a:
            a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome):
    try:
        a = open(nome, 'x')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f"Arquivo {nome} criado com sucesso!")



def addpessoa(arq, nome, idade):
    try:
        a = open(arq, 'at')

    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        """valido = False
        nome = str(input("Nome: "))
        while not valido:
            nome.replace(',', '.').strip()
            if nome.isnumeric() or nome == '':
                print(f"\033[31mERRO, DIGITE UM NOME VÁLIDO!\033[m")
            else:
                valido = True"""
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um ERRo na hora de escrever os dados!")
        else:
            menu__init__.cabecalho('CADASTRO EFETUADO COM SUCESSO!')
            a.close()
        """while True:
            idade = str(input("Idade: ")).strip()
            if idade.isalpha() or idade == '':
                print(f"\033[31mERRO, DIGITE UMA IDADE VÁLIDA!\033[m")
                continue
            else:
                int(idade)
                a.write(idade.rjust(50 - len(nome)))
                a.write(' anos')
                a.write('\n')
                break"""


def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Houve um ERRO ao ler o arquivo!')
    else:
        menu__init__.cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()




