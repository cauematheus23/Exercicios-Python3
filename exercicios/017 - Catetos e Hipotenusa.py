"""   Faça um programa que leia o comprimento do cateto oposto e do catetp adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.   """
from math import hypot
co = float(input("Comprimento do Cateto oposto: "))
ca = float(input("Comprimento do cateto adjascente: "))
hi = hypot(co,ca)
print(f"A hipotenusa vai medir {hi:.2f}")