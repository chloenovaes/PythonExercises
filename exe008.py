"""Desafio 008 - Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

n = int(input('Digite o valor em metros: '))
print(f'O valor digitado em metros foi {n}. Em centímetros, o valor é de {n*100} e em milímetros o valor é de {n*1000}.')

"""Pedido extra do exercicio para transformar em Km / Hm / Dam / Dm """
n = int(input('Digite o valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
print(f'O valor digitado em metros é {n}. O valor em Km é {n/1000}, o valor em Hm é {n/100}, o valor em Dam é {n/10} e '
      f'o valor em Dm é {n*10}.')