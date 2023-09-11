'''   Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("="*30,end='')
print("BANCO DO KUDSA",end='')
print("="*30)
while True:
    val = int(input("Qual valor gostaria de sacar: "))
    s50 = val //50
    s20 = (val - (s50*50 ))//20
    s10 = (val - (s50*50 + s20*20))//10
    s01 = (val - (s50*50 + s20*20+ s10*10))//1
    break
print(f"TOTAL DE {s50} CÉDULAS DE R$50\nTotal de {s20} cédulas de R$20\nTotal de {s10} cédulas de R$10\nTotal de {s01} cédulas de R$1")
print("="*30)
print("VOLTE SEMPRE AO BANCO DO KUDSA")