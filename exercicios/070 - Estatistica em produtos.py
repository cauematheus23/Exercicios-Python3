"""   Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.   """


menor = 0
tot = 0 
a = 'S'
cont = 0
while a == 'S':
    print("="*30,end='')
    print("LOJA DE COMPRAS",end='')
    print("="*30)
    prod = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço: "))
    tot += preco
    if menor < preco:
        menor = prod
    menor = preco
    if preco > 1000:
        cont +=1
    a = str(input("Deseja continuar ? [S/N]")).upper()
    while a != 'S' and a != 'N':
        print("Codigo invalido digite novamente")
        a = str(input("Deseja continuar ? [S/N]")).upper()
print(f"Compra finalizada com o total de {tot}")
print(f"{cont} produtos custam mais de 1000 reais")
print(f"O produto mais barato é {menor}")