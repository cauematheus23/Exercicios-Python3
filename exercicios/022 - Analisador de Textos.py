"""   Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome.   """
nome = str(input("Qual seu nome: "))
pnome = nome.split()
letras = 0
for c in nome:
    if c.isalpha():
        letras +=1
print('='*160)
print("O PROGRAMA A SEGUIR IRA MOSTRAR SEU NOME COM TODAS AS LETRAS MAIUSCULAS, MINUSCULAS, QUANTAS LETRAS TEM AO TODO E QUANTAS LETRAS TEM APENAS SEU PRIMERO NOME")
print('='*160)
print(nome.upper())
print(nome.lower())
print(letras)
print(len(pnome[0]))