"""   Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido   """
import random
a1 = str(input("Nome do aluno: "))
a2 = str(input("Nome do aluno: "))
a3 = str(input("Nome do aluno: "))
a4 = str(input("Nome do aluno: "))
lista = [a1,a2,a3,a4]
print(f"O escolhido foi {random.choice(lista)}")