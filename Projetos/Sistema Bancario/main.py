menu = """

[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(f"Escolha a opção: {menu}").upper()

    if opcao == 'D':
        print("Depositar")

        valor = float(input("Digite o valor a ser depositado: "))
    elif opcao == "S":
        print("Sacar")
        valor = float(input("Digite o valor a ser sacado: "))

    elif opcao == "e":
        print("Extrato")

    elif opcao == "Q":
        print("Sair")
        break
    
    else:
        print("Opção inválida")
        continue






