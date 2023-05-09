import textwrap,os

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
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso!\n===")
    else:
        print("\n@@@Operação falhou! o valor informado é invalido.@@@\n")

    return saldo,  extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Flag
    excedeu_saldo = valor > saldo # Flag
    excedeu_limite = valor > limite # Flag
    excedeu_saque = numero_saques >= limite_saques # Flag
    sacar = valor > 0 # Flag

    # Verificar se o usuário já realizou 3 saques
    if excedeu_saldo:
        extrato = extrato + f"\nTentativa de saque de R$ {valor:.2f}"
        print(f"\n@@@Operação falhou! Saldo de: {saldo}.\n insuficiente.@@@\n")

    elif excedeu_saque:
        extrato = extrato + f"\nTentativa de saque de R$ {valor:.2f}"
        print('\n@@@Operação falhou! Limite de 03 saque diário atingido.@@@\n')

    # Verificar se o usuário já realizou 3 saques
    elif excedeu_limite:
        extrato = extrato + f"\nTentativa de saque de R$ {valor:.2f} (limite de 500 excedido)"
        print("\n@@@Operação falhou! Limite de saque diário atingido.@@@\n")

    # Verificar se o usuário já realizou 3 saques
    elif sacar:
        saldo -= valor
        extrato += f"\nSaque: {valor:.2f} realizado com sucesso!\n"
        numero_saques += 1
        print("\n===Saque realizado com sucesso!\n===")
    else:
        print("\n@@@Operação falhou! o valor informado é invalido.@@@\n")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*,extrato): # Parâmetros obrigatórios, opcionais e nomeados (posicional e nomeado)
    print("\n=============Extrato=============\n")
    # Verificar se o extrato está vazio e exibir uma mensagem para o usuário caso esteja vazio
    print("Não foram realizadas movimentações\n") if extrato == "" else print(extrato) # Operador ternário
    print(f"Saldo: {saldo:.2f}\n")
    print("=================================\n")
    
    print("\n=============Salvar Extrato=============\n")
    try:
        file_extrato = str(input("Nome do arquivo: ")).upper()
                
    except Exception as e:
        print("Erro: ", e)
        
    verifica_arquivo = os.path.exists(f'Projetos Trilha Dio Python/Otimizando o Sistema Bancário com Funções Python/extratos/{file_extrato}.txt')
    valida_nome_null = file_extrato == ""

    if valida_nome_null:
        print("Nome inválido")
    if verifica_arquivo:
        print("Arquivo já existe") 

    # Caso o arquivo não exista, criar um arquivo com o nome digitado pelo usuário
    else:
        # Criar um arquivo de texto com o extrato da conta do usuário
        arquivo = open(f'Projetos Trilha Dio Python/Otimizando o Sistema Bancário com Funções Python/extratos/{file_extrato}.txt','w') # Abrir o arquivo
        arquivo.write(extrato) # Escrever o extrato no arquivo
        arquivo.close() # Fechar o arquivo    
    print("\n=================================\n")


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
        try:
            opcao = menu().upper()

        except Exception as e:
            print("Erro: ", e)
        

        if opcao == 'd'.upper():
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s".upper():
            print('sacar valor') # Teste
            valor = float(input("Digite o valor a ser sacado: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            
        
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




















