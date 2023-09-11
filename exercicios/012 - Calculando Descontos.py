"""   Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto   """
produto = str(input("Produto: "))
preço = float(input(f"Qual o preço de {produto}: "))
desconto = preço - (preço * 0.05)
print(f"{produto} com 5% de desconto ficou no total de {desconto:.2f}")