"""    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO   """

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
print(f'Sua média foi {media :.1f}')
if media < 5:
    print('\033[4;31mREPROVADO\033[m ')
elif 7 > media >=5:
    print('\033[4;33mRECUPERAÇÃO\033[m ')
elif media >= 7:
    print('\033[4;34mAPROVADO\033[m ')
