"""   Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.   """
km = float(input("Quantos Km foram percorridos com o veiculo? "))
dias = int(input("Quantos dias ficou com ele? "))
preço = (dias * 60) + (km * 0.15)
print(f"O carro foi alugado por {dias} dias e percorreu {km} e o valor total ficou em R${preço}.")