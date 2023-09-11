"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
lista = [[], []]
for c in range (1,8):
    a = int(input(f"Digite o {c}° valor: "))
    if a % 2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)

lista[0].sort()
lista[1].sort()
print("="*30)
print(f"Os numeros impares são {lista[1]}")
print(f"Os numeros pares são {lista[0]}")