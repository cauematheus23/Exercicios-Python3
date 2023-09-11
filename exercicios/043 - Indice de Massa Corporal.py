"""   Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida  """

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é \033[34m{imc :.1f}\033[m e a classificação é: \033[34mAbaixo do Peso\033[m')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é \033[34m{imc :.1f}\033[m e a classificação é: \033[34mPeso Ideal\033[m')
elif 25 <= imc < 30:
    print(f'Seu IMC é \033[34m{imc :.1f}\033[m e a classificação é: \033[34mSobrepeso\033[m')
elif 30 <= imc < 40:
    print(f'Seu IMC é \033[34m{imc :.1f}\033[m e a classificação é: \033[34mObesidade\033[m')
else:
    print(f'Seu IMC é \033[34m{imc :.1f}\033[m e a classificação é: \033[34mObesidade Mórbida\033[m')
