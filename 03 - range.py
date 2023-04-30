"""

for + Range
range -> gera uma sequencia numerica range(start, stop, step)

"""
number_par = []
number_impar = []

while True:
    entrada = int(input('Digite um numero de 1 a 10: '))
    sair = str(input('Deseja sair? [s/n] ').lower())

    if sair == 's':
        break

    if entrada % 2 == 0:
        number_par.append(entrada)
        for point in range(len(number_par)):
            print(number_par[point])

    elif entrada % 2 != 0:
        number_impar.append(entrada)
        for point in range(len(number_impar)):
            print(number_impar[point])

 
    else:
        print('Numero invalido')
    

print(f'Numeros pares{number_par}\nnumeros impares{number_impar}')

quit()
# Exemplo 1
for x in range(-1, -101, -1):

    print(x)


