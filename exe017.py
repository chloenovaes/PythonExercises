"""Desafio 018 - Catetos e Hipotenusas
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa."""

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')

#Solução sem importação da biblioteca Math:
#hi = (co**2 + ca**2) ** (1/2)
#print(f'A hipotenusa vai medir {hi:.2f}')