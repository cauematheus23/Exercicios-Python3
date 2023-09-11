
def linha():
    print('-'*42)

def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mTipo invalido, digite  um numero inteiro valido.\033[m ")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuario")
            return 0
            break
        else:
            return a

def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha()
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaint('\033[33mSua Opção:\033[m ')
    return opc


