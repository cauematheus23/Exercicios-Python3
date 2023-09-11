"""   Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento   """
nome = str(input("Nome do funcionario: "))
s = float(input(f"Qual o salário de {nome}: "))
novos = s + (s * 0.15)
print(f"O novo salário de {nome} que era {s} agora com 15% de aumento passou a ser {novos}")