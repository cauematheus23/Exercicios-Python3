"""   Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros   """

print('-='*40)
print(' ' *35,end= '')
print(f'\033[35mLOJAS KUDSA\033[m')
print('-='*40)
produto = float(input('Digite o valor do produto: '))
dinheiro = produto * 0.1
cartao = produto * 0.05
cartao1 = produto * 0.2
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pay = int(input('Qual é a opção de pagamento? '))

if pay == 1:
        val = produto - dinheiro
        print(f'O valor do produto original é \033[34mR${produto:.2f}\033[m com o desconto de 10% ficou \033[34mR${val:.2f}\033[m')
elif pay == 2:
        val = produto - cartao
        print(f'O valor do produto original é \033[34mR${produto:.2f}\033[m com o desconto de 5% ficou \033[34mR${val:.2f}\033[m')
elif pay == 3:
        print(f'Você escolheu parcelar \033[34m{produto :.2f}\033[m em \033[34m{2}\033[mx \ncada parcela sairá por \033[34mR${produto / 2 :.2f}\033[m \nvalor total a ser pago pelo produto sera de \033[34mR${produto :.2f}\033[m')
elif pay == 4:
        parcela = int(input('Gostaria de parcelar em quantos meses? '))
        val = produto + cartao1
        print(f'Você escolheu parcelar \033[34m{produto :.2f}\033[m em \033[34m{parcela}\033[m meses \ncada parcela sairá por \033[34mR${val / parcela :.2f}\033[m \no valor total a ser pago pelo produto com juros sera de \033[34mR${val :.2f}\033[m')

