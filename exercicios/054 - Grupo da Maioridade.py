"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
menores = 0
for c in range(1,8):    
    nasc = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    if date.today().year - nasc < 21:
        menores +=1
print(f"{menores} ainda não atingiram a maioridade")
print(f"Apenas {7 -menores} alcancaram a maioridade")
