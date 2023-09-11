""""   Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.  """
n = int(input("Digite um número entre 0 e 9999: "))

print(f"Milhar: {n // 1000 }")
print(f"Centena: {n // 100 % 10}")
print(f"Dezena: {n // 10 % 10}")
print(f"Unidade: {n // 1 % 10}")
