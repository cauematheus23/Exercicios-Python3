"""   Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8   """

cont = 3
n = int(input("Digite quantos termos da sequencia quer mostrar: "))
a = 0
b = 1
print('~'*30)
print('SEQUENCIA DE FIBONACCI')
print('~'*30)
print('\033[34m{}\033[m -> \033[34m{}\033[m'.format(a, b),end= '')
while cont <= n:
    c = a + b
    print(' -> \033[34m{}\033[m'.format(c),end='')
    a = b
    b = c
    cont += 1
print('-> \033[30mFIM!\033[m')
print('~'*30)