""" Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo   """
import math
angulo = int(input("Digite o valor o angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"Dado o angulo {angulo:.2f}, seu seno é {sen:.2f}, seu cosseno é {cos:.2f} e a tangente é {tan:.2f}")