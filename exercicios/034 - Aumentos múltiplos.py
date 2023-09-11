"""   Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salarios superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.   """
salario = float(input('Digite o valor do salario para calcularmos o aumento: '))
if salario <= 1250:
    salario = salario + (salario * 0.15)
    print(f'Parabens você ganhou um aumento de 15% seu novo salario é R${salario:.2f}')
else:
    salario = salario + (salario * 0.10)
    print(f'Parabens você ganhou um aumento de 10% seu novo salario é R${salario:.2f}')