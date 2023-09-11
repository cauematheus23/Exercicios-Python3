""" Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros   """

n1 = float(input("Digite uma medida a ser convertida: "))
mm = n1 * 1000
cm = n1 * 100
print(f"{n1} metros é igual a {cm:.0f} centimetros e {mm:.0f} milimetros")