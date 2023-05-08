import os # Importar o módulo os para verificar se o arquivo existe
menu = """

[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

"""
# Variáveis
saldo = 0 # Variável
limite = 500 # Constante
extrato = "" # Acumulador
numero_saques = 0 # Contador
LIMITE_SAQUES = 3 # Constante




# Início do programa
while True:
    # Apresentar o menu de opções para o usuário e solicitar a opção desejada pelo usuário (input)
    # Tratar o erro caso o usuário digite uma opção inválida
    try:
        opcao = input(f"Escolha a opção: {menu}").upper()
    except Exception as e:
        print("Erro: ", e)

    # Verificar qual opção o usuário escolheu e executar a ação correspondente
    if opcao == 'd'.upper():
        try:
            valor = float(input("Digite o valor a ser depositado: "))
        except Exception as e:
            print("Erro: ", e)
            continue

        # Verificar se o valor digitado é um número diferente de float
        verifica_deposito = type(valor) != float

        if verifica_deposito:
            print("Valor inválido")
            continue
        else:
            saldo += valor # Atualizar o saldo
            extrato = extrato + f"\nDepósito de R$ {valor:.2f}" # Atualizar o extrato
            print(f"\nValor de R$ {valor:.2f} depositado com sucesso\n\nSeu saldo agora e de R$ {saldo:.2f}")

    elif opcao == "s".upper():
        # Verificar se o usuário já realizou 3 saques
        excedeu_saque = numero_saques == LIMITE_SAQUES # Flag

        if excedeu_saque:
            print("Limite de saques atingido")
            extrato = extrato + f"\nTentativa de saque (limite de saque diario atingido)"
            continue
        else:
            try:
                valor = float(input("Digite o valor a ser sacado: "))
            except Exception as e:
                print("Erro: ", e)
                continue


            # Verificar se excedeu o limite de saque diário (R$ 500) 
            excedeu_limite = valor > limite # Flag

            # Verificar se excedeu o saldo
            excedeu_saldo = valor > saldo # Flag

            if excedeu_limite:
                extrato = extrato + f"\nTentativa de saque de R$ {valor:.2f} (limite excedido)"
                print("Limite de saque excedido (R$ 500)")
                continue

            # Verificar se e possivel realizar o saque (saldo > 0 e valor <= saldo).
            saque = saldo > 0 and valor <= saldo

            # verificar se o saldo é maior que zero e se o valor é menor ou igual 
            # ao saldo disponível na conta do usuário e realizar o saque caso as condições sejam atendidas
            # Caso contrário, informar o usuário que o saldo é insuficiente ou que o valor é inválido
            if saque:
                saldo -= valor
                extrato = extrato + f"\nSaque de R$ {valor:.2f}"
                print(f"\nValor de R$ {valor:.2f} sacado com sucesso\n\nSeu saldo agora e de R$ {saldo:.2f}")
                numero_saques += 1

            elif excedeu_saldo:
                print("Saldo insuficiente")
                extrato = extrato + f"\nTentativa de saque de R$ {valor:.2f}"
            else:
                print("Valor inválido")

    elif opcao == "e".upper():
        try:
            file_extrato = str(input("Nome do arquivo: ")).upper()
                
        except Exception as e:
            print("Erro: ", e)
        
        verifica_arquivo = os.path.exists(f'Projetos Trilha Dio Python/Criando um Sistema Bancário com Python/{file_extrato}.txt')
        valida_nome_null = file_extrato == ""

        if valida_nome_null:
            print("Nome inválido")
            continue
        # Verificar se o arquivo já existe
        if verifica_arquivo:
            print("Arquivo já existe") 
            continue # Caso o arquivo já exista, solicitar um novo nome para o arquivo

        # Caso o arquivo não exista, criar um arquivo com o nome digitado pelo usuário
        else:
            # Criar um arquivo de texto com o extrato da conta do usuário
            arquivo = open(f'Projetos Trilha Dio Python/Criando um Sistema Bancário com Python/{file_extrato}.txt','w') # Abrir o arquivo
            arquivo.write(extrato) # Escrever o extrato no arquivo
            arquivo.close() # Fechar o arquivo
            print("Extrato") # Apresentar o extrato na tela
            print(extrato,"\n",f"Seu saldo é de R$ {saldo:.2f}") # Apresentar o saldo na tela

    elif opcao == "q".upper():
        print("Sair")
        print("Volte sempre")
        print(f"Seu saldo final é de R$ {saldo:.2f}")
        break
    else:
        print("Opção inválida")






