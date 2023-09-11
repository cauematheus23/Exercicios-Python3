"""   Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. Pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salario ou entãoo empréstimo será negado.  """
sim = str(input('Você deseja comprar uma casa? responda com sim ou não '))
if sim == 'sim' or 'Sim' or 's' or 'SIM':
    casa = float(input('Qual o valor da casa? '))
    salario = float(input('Qual seu salário? '))
    anos = int(input('Em quantos anos pretende pagar? ')) * 12
    prest = casa / anos
    if prest > salario * 0.3:
        print('Sentimos muito mas você não pode fazer o emprestimo')
    else:
        print('Parabéns você consegue financiar uma casa')
else:
    print('Tenha um bom dia =)')



