"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""
def leiaint(msg):
    n=input(msg)
    while type(n) != int:
        if n.isnumeric()==False:
            print('Não foi digitado um número inteiro!')
            n=input('Digite um número: ')         
        else:       
            n=float(n)
            if n.is_integer()==False:
                print('Não foi digitado um número inteiro!')        
                n=input('Digite um número: ')
            else:
                n=int(n)
    return n