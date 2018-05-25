"""Desafio 012 - Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

preço = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${preço-(preço*5/100):.2f}.')
