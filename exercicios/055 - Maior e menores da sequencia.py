"""   Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.   """
lista = []
for c in range (0,5):
    pessoa = int(input("Digite o peso: "))
    lista.append(pessoa)

print(f"O maior peso lido foi {max(lista)}Kg")
print(f"O menor peso lido foi {min(lista)}Kg")