"""
Iteravel -> String, Lista, Range, Tupla, Dicionario
Iterador -> Funcao que itera sobre um iteravel
next -> Me entreguie o proximo valor 
iter -> Me entregue seu iterador

"""


text = 'van'
iterador = iter(text)



while True:
    # Tratamento de erro para parar o loop quando o iterador acabar 
    try:
        # Printar o proximo valor do iterador
        print(next(iterador)) # next() -> __next__()
    # StopIteration -> Erro que para o loop
    except StopIteration:
        break

quit() # Para o codigo
# Outra forma de fazer o mesmo codigo acima porem mais simples e não mostra tudo de uma vez
print(iterador.__next__())

texto = iter('Python') # __iter__()
print(texto.__next__()) # __next__()
print(next(texto)) # next()