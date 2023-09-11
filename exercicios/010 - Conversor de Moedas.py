""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.  (Considere o dolar a 3.27 R$) """
real = float(input("Quantos reais você tem:  "))
dolar = real / 3.27

print(f"Com {real} reais você pode comprar {dolar:.2f} dolares.")