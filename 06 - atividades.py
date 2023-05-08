''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
a = input() 
b = input() 
c = input()

# Flag para verificar se o animal é um vertebrado
vertebrado = a == 'vertebrado'
ave = b == 'ave'
carnivoro = c == 'carnivoro'
onivoro = c == 'onivoro'
inseto = b == 'inseto'
hematofago = c == 'hematofago'

if vertebrado:
    if ave:
        if carnivoro:
            print('aguia')
        else:
            print('pomba')
    else:
        if onivoro:
            print('homem')
        else:
            print('vaca')
else:
    if inseto:
        if hematofago:
            print('pulga')
        else:
            print('lagarta')
    else:
        if hematofago:
            print('sanguessuga')
        else:
            print('minhoca')