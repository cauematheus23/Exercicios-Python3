"""   Faça um programa que leia três números e mostre qual é o maior e qual é o menor.  """
"""lista = []
for c in range (0,3):
    v = int(input("Digite um valor: "))
    lista.append(v)
    if c == 0:
        maior = menor = lista[c] # define como o primeiro valor da lista
    else: 
        if lista[c] > maior: #verificar se os proximos valores são maiores ou menores.
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f"\033[31mMaior é {maior} e Menor é {menor}\033[m")"""

# ou

l2 = []
for c in range(0,3):
    a = int(input("Digite um valor: "))
    l2.append(a)
l2.sort()
print(f"Maior valor é {l2[2]} e o Menor é {l2[0]}")