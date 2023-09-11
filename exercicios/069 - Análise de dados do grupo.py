"""   Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.   """

contm= 0
contf= 0 
contidade= 0
a = 'S'
while a == 'S' or a == 'SIM':
    print('='*15,end='')
    print('CADASTRE UMA PESSOA',end='')
    print('='*15)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]")).upper()
    if idade > 18:
        contidade += 1
    if sexo == 'M' or sexo == "MASCULINO":
        contm +=1
    if idade < 20 and sexo == "F" "FEMININO":
        contf =+ 1
    a = str(input("Quer continuar? [S/N]")).upper()
print(f"{contidade} pessoas tem mais de 18 anos, {contm} homens foram cadastrados, {contf} são mulheres com menos de 20 anos")
