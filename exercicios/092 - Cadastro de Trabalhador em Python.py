"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
import datetime
empregado = {'Nome':str(input("Nome: ")),'idade':int(input('Ano de Nascimento: ')),'ctps': int(input("N° Carteira de trabalho(0 = não tem): "))}
if empregado['ctps'] == 0:
    empregado['idade'] = datetime.date.today().year - empregado['idade']
    print('-='*30)
    print(empregado)
    for k , v in empregado.items():
        print(f'{k} tem valor {v}')
else: 
    empregado['contratação'] = int(input('Ano de contratação: '))
    empregado ['salário'] = float(input("Salário: R$ " ))
    empregado ['aposentar'] = (empregado['contratação'] - empregado ['idade']) + 35
    empregado['idade'] = datetime.date.today().year - empregado['idade']
    print('-='*30)
    print(empregado)
    for k, v in empregado.items(): 
        print(f"{k} tem valor {v}")
print('-='*30)