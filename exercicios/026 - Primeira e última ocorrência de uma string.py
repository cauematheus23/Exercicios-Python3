""" Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra A
    - Em que posição ela aparece a primeira vez.
    - Em que posição ela aparece a última vez.  """
f = str(input("Digite uma frase que esteja pensando: ")).lower()
print(f"A letra A aparece {f.count('a')} vezes")
print(f"A letra A aparece pela primeira vez na posição {f.find('a')+1}")
print(f"A letra A aparece pela ultima vez na posição {f.rfind('a')+1}")