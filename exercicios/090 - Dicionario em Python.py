"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
aluno = {'Nome' : str(input('NOME: ')),'Media' : int(input(f"Média: "))}
if aluno['Media'] < 5:
    aluno['Situação'] = 'REPROVADO'
else:
    aluno['Situação'] = 'APROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')