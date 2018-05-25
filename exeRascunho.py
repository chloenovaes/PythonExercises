dicionario = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
              'mercado', 'programador', 'futuro')
for palavra in dicionario:
    z = ''
    for letra in palavra:
        if letra in 'aeiou':
            z += f'{letra} '
    print(f'Na palavra {palavra.upper()} temos', z)﻿

