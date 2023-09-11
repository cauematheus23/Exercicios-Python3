"""   Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente.   """
n = str(input("Digite seu nome: ")).split()
print(f"Bem Vindo!\nSeu primeiro nome é {n[0]}\nSeu ultimo nome é {n[-1]} ")
