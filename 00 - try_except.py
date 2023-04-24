"""
Introdução ao try/except

try --> tentar executar o código
except --> caso haja erro, executar o código

"""


print(123)

while True:
    try:
        x = int(input('Digite um número: '))
        print(f'O dobro de {x} é {x * 2}')
        break
    except ValueError:
        print('Valor inválido. Tente novamente.')
    
'''
Lembrando que essa não e a melhor forma de se fazer isso, pois o ideal é que o usuário não veja o erro, mas sim uma mensagem amigável.

'''

