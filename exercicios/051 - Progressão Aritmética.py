"""   Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.   """

pt = int(input("Digite o primeiro termo da P.A: "))#Primeiro termo da P.A
rp = int(input("Digite a Razão dessa P.A: "))#Razao da P.A
rep = pt +(11-1) * rp #Formula pra se achar o decimo termo da P.A
for c in range(pt,rep,rp):
    print('{} '. format(c), end ='-> ')
print('acabou')