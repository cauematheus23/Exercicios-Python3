"""   Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR OU IMPAR.   """
n = int(input("Digite um numero inteiro aleatorio: "))
par = n % 2
if par == 0 :
    print("O numero digitado é PAR")
else:
    print("O numero digitado é IMPAR")