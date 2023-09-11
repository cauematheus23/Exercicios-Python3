"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """
l = []
while True:
    b = (int(input("Digite um valor: ")))
    if b not in l:
        l.append(b)
    else:
        print("Valor duplicado")
    r = str(input("Quer continuar? [S/N]"))
    if r in 'Nn':
        break
print('='*30)
l.sort()
print(f"Você digitou os valores {l}")

