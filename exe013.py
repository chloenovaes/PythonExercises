"""Desafio 013 - Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

salario = float(input('Qual é a salário do funcionário? '))
aumento = salario + (salario*15/100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento passa a receber R${aumento:.f}')