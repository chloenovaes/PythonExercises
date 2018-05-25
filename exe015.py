"""Desafio 015 - Aluguel de Carros
Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
preço = (dias*60) + (km*0.5)
print(f'O total a pagar é de R${preço:.2f}')
