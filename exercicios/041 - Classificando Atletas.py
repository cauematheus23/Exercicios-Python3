"""   A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER   """

from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc
if idade <= 9:
    print('Classificação: \033[35mMIRIM\033[m ')
elif 9 < idade <= 14:
    print('Classificação: \033[34mINFANTIL\033[m ')
elif 14 < idade <= 19:
    print('Classificação: \033[33mJÚNIOR\033[m ')
elif 19 < idade <= 25:
    print('Classificação: \033[32mSÊNIOR\033[m ')
else:
    print('Classificação: \033[31mMASTER\033[m ')
