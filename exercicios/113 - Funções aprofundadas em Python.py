"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""
def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mTipo invalido, digite  um numero inteiro valido.\033[m ")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuario")
            return 0
            break
        else:
            return a


def leiaFloat(msg):
    while True:
        try:
            a = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mTipo invalido, digite  um numero real valido.\033[m ")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuario")
            return 0
            break
        else:
            return a


n = leiaint("digite número inteiro: ")
n1 = leiaFloat(("Digite um número Real: "))
print(f"O numero inteiro digitado foi \033[34m{n}\033[m e o real \033[34m{n1}\033[m")
