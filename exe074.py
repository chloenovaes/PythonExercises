from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0,10), randint(0, 10), randint(0, 10))
print(f'O valores sorteados foram: {lista}')
maior = 0
menor = 10
for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
