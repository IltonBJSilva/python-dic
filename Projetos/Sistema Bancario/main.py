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

    try:
        opcao = input(f"Escolha a opção: {menu}").upper()
    except Exception as e:
        print("Erro: ", e)

    if opcao == 'D':
        print("Depositar")
        try:
            valor = float(input("Digite o valor a ser depositado: "))
        except Exception as e:
            print("Erro: ", e)
            continue

        if type(valor) != float:
            print("Valor inválido")
            continue
        else:
            saldo += valor
            print(f"\nValor de R$ {valor:.2f} depositado com sucesso\n\nSeu saldo agora e de R$ {saldo:.2f}")

    elif opcao == "S":
        print("Sacar")



    elif opcao == "e":
        print("Extrato")

    elif opcao == "Q":
        print("Sair")
        print("Volte sempre")
        print(f"Seu saldo final é de R$ {saldo:.2f}")
        break
    else:
        print("Opção inválida")






