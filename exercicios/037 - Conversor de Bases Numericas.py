"""   Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.   """

a = int(input('Digite um numero inteiro: '))
b = int(input('Digite uma base de conversão, 1 para binario, 2 para octal, 3 para hexadecimal '))
if b == 1:
    print(f'O número {a} convertido em binário fica: {bin(a)[2:]}')
elif b == 2:
    print(f'O número {a} convertido em octal fica: {oct(a)[2:]}')
elif b== 3:
    print(f'O número {a} convertido em hexadecimal fica: {hex(a)[2:]}')
else: 
    print("OPÇÃO INVALIDA.TENTE NOVAMENTE")
