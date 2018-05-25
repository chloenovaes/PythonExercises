"""Desafio 006 - Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

import math
n = int(input('Digite um número: '))
print(f'O valor digitado foi {n}. O dobro é {n*2}, o triplo é {n*3} e a raiz quadrada é {math.sqrt(n):.2f}.')
