"""Desafio 016 - Quebrando um Número
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira."""

from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {math.trunc(n)}')

#Resolução alternativa do Prof. Guanabara
#num = float(input('Digite um valor: ')
#print('O valor digitado foi {num} e a sua porção inteira é {int(num)}'
