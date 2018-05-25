"""Desafio 020 - Sorteando uma Lista
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle
n1 = str(input('Primeiro Aluno: ')).strip().upper()
n2 = str(input('Segundo Aluno: ')).strip().upper()
n3 = str(input('Terceiro Aluno: ')).strip().upper()
n4 = str(input('Quarto Aluno: ')).strip().upper()
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')