"""   Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.   """
v = float(input("Qual a distancia em Km da viagem a ser feita: "))
if v <= 200:
    print(f"A passagem ira custar R${v * 0.50}")
else:
    print(f"A passagem ira custar R${v * 0.45}")
