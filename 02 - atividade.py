''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input("Digite o número de casos de teste: "))

while(N > 0):
  # Recebe os valores de entrada
  v = input().split() # split() separa os valores de entrada por espaço em branco
  a = v[0] # v[0] é o primeiro valor de entrada
  b = v[1] # v[1] é o segundo valor de entrada

  # Verifica se o segundo valor de entrada está contido no primeiro valor de entrada
  if len(b) > len(a):
    print("nao encaixa")
  # Verifica se o segundo valor de entrada está contido no primeiro valor de entrada
  elif a.endswith(b):
    print("encaixa")
  # Caso contrário, o segundo valor de entrada não está contido no primeiro valor de entrada
  else:
    print("nao encaixa")
  N -= 1