"""   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.   """

s = str(input("Qual seu sexo?\nDigite M para Masculino e F para Feminino: ")).upper()
while s not in 'M' 'F' 'm' 'f':
    s = str(input("Sexo Digitado invalido por favor digite novamente: "))
if s == 'M' 'm':
    print("Sexo cadastrado {}asculino".format(s))
else:
    print("Sexo cadastrado {}eminino".format(s))