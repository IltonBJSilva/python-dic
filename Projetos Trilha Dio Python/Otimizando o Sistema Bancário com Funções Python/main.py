import textwrap

def menu():
    menu = """\n
    ==============================MENU==============================
    [LS] - Listar usuários
    [LC] - Listar contas
    [CS] - Criar usuário
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
    ================================================================
    """
    return menu

def depositar(saldo, valor, extrato):
    pass

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass

def exibir_extrato(saldo,/,*,extrato):
    pass


def criar_usuario(usuario):
    pass

def filtrar_usuario(cpf, usuario):
    pass

def criar_conta(agencia, numero_conta, usuario):
    pass

def listar_contas(contas):
    for conta in contas:
        print(conta)
        # linha 
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            
            
            """
    pass

def main():
    LIMITE_SAQUES = 3 # Constante
    AGENCIA = '0001' # Constante


    saldo = 0 # Variável
    limite = 500 # Constante
    extrato = "" # Acumulador
    numero_saques = 0 # Contador

    usuario = []
    contas = []



    while True:
        opcao = menu()
        try:
            opcao = input(f"{menu()}Escolha: ").upper()

        except Exception as e:
            print("Erro: ", e)
        

        if opcao == 'd'.upper():
            print('depositar valor') # Teste
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

            break

        elif opcao == "s".upper():
            print('sacar valor') # Teste
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            break
        
        elif opcao == "e".upper():
            print('extrato') # Teste
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "q".upper():
            print('sair') # Teste
            break
        elif opcao == "ls".upper():
            print('listar usuários') # Teste
            break
        elif opcao == "lc".upper():
            print('listar contas') # Teste
            break
        elif opcao == "cs".upper():
            print('criar usuário') # Teste
            criar_usuario(usuario)
            break
        else:
            print('Opção inválida')
            break



main()




















