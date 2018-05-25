extenso = 'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',\
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num <0:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[num]}')

#Resolução do Prof. Guanabara:
#cont = 'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',\
   # 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
#while True:
    #núm = int(input('Digite um número entre 0 e 20: '))
    #if 0 <= núm <= 20:
        #break
    #print('Tente novamente.', end='')
#print(f'Você digitou o número {cont[núm]}')
