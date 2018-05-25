"""Desafio 011 - Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input('Largura da Parede em Metros: '))
altura = float(input('Altura da Parede em Metros: '))
área = largura*altura
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {área}m².')
print(f'Para pintar essa parede, você precisará de {área/2:.2f}L de tinta.')
