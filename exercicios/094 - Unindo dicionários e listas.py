"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
'''cadastro = []
pessoas = dict()
mulheres = []
amedia = []
media = 0
while True: 
    pessoas['nome'] = str(input("Nome: "))
    pessoas['sexo'] = str(input("Sexo: [M/F] ")).upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    media +=  pessoas['idade']
    cadastro.append(pessoas.copy())
    i = str(input("Deseja cadastrar outra pessoa? [S/N] "))
    if i in 'Nn': 
        break
media = media / len(cadastro)
for k,v in enumerate(cadastro):
    if cadastro[k]['sexo'] in "Ff":
        mulheres.append(cadastro[k]['nome'])
for k,v in enumerate(cadastro):
    if cadastro[k]['idade'] > media :
        amedia.append(cadastro[k])
print('-='*30)
print(f"- Foram cadastradas {len(cadastro)} pessoas")
print(f"- A média de idade foi {media:.2f}")
print(f"- As mulheres cadastradas foram {mulheres}")
print(f"- As pessoas com idade acima da media foram {amedia}")'''
galera = list()
pessoa = dict()
soma = media = 0
while True: # COLETA DE DADOS
    pessoa.clear()
    pessoa['nome'] = str (input('Nome: '))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ").upper()[0]) # VALIDAÇÃO DE SEXO
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por Favor digite apenas M ou F.")
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True: # VALIDAÇÂO CONTINUAR
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break
print('-='*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A media de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram", end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end='')
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in galera:
    if p['idade'] >=media:
        print('     ', end='')
        for k, v in p.items():
            print(f"{k}= {v}", end='')
        print()
print("<< ENCERRADO >>")