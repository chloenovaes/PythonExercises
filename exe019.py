"""Desafio 019 - Sorteando um Ítem na Lista
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice
a = str(input('Primeiro Aluno: ')).upper().strip()
b = str(input('Segundo Aluno: '))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))
lista = [a, b, c, d]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
