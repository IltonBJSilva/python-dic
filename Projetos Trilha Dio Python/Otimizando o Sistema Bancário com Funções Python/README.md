
# Sistema Bancario

Fomos contratados por um grande banco para desenvolver o seu novo sistema. 

Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações:

1.  Depósito.
2.  Saque.
3.  Extrato.

## Como funciona

### Operação de Depósito

 - Deve ser possível depositar valores positivos para a minha conta
   bancaria, a v2 do projeto trabalha mais de um usuário, dessa forma
   precisamos nos preocupar em identificar qual é o número da
   agência e conta bancaria. Todos os depósitos devem ser armazenados em
   uma variável e exibidos na operação de extrato.

### Operação de Saque

 - O sistema deve permitir realizar 3 saques diário com limite máximo de
   R$ 500,00 por saque. Caso o usuário não tenha saldo em conta,  o   
   sistema deve exibir uma mensagem informando que não será possivel   
   sacar o dinheiro por falta de saldo. Todos os saques devem ser   
   armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato

 - Essa operação deve listar todos os depósitos e saques realizados na
   conta. No fim da listagem deve ser exibido o saldo atual da conta.
   
 - Os valores devem ser exibidos utilizando o formatado R$ xxx:xx,   
   Exemplo:
      1500.45 = R$ 1500.45

## Otimizando Sistema bancario com novas atualizações 

#### Objetivo Geral

 - Separar as funções existentes de Saque, depósito e extrato em funções.
 - Criar duas novas Funções: Cadastrar usuário (Cliente) e cadastrar conta bancária.

### Desafio
- Precisamos deixar nosso código mais moduralizado, para isso vamos criar funções para as operações existentes: sacar, depositar e extrato. Além disso,  para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (Cliente do banco) e criar conta corrente (vincular com usuário).

### Separação em funções
- Devemos criar funções para todas as operações do sistema. para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por mim na forma que eu achar melhor

#### Saque
- A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldos, valor, extrato, limite,  numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

#### Depósito
- A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

#### Extrato
- A função extrato deve receber os argumentos por posição e nome, (Positional only e keyword only.) Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Novas funções
- precisamos criar duas novas funções: criar usuário e criar conta corrent. Fique a vontade para adicionar mais funções, exemplo:
	- Listar contas.
	- Listar usuario
	- Inativar conta
#### Criar usuário
- O programa deve armazenar os usuário em uma lista, um usuário é composto por:
	- Nome
	- Data de nascimento (dd/mm/aaaa)
	- CPF (Somento numero)
	- endereço
- O endereço é uma string com o formato:
	- Logradouro,
	- nro
	- bairro
	- cidade/sigla
	- estado
- Deve ser armazenado somento os números do CPF. não podemos cadastar 2 usuário com o mesmo CPF.

#### Criar Conta corrente
- O programa deve armazenar contas em uma lista, uma conta é composto por:
	- Agência
		- Fixo --> 0001
	- Numero da conta do usuario
		- Numero da conta e sequencial começado em 1
	- Usuario pode ter mais de uma conta,  porem uma conta pertence a somente um usuário
	- endereço
- O endereço é uma string com o formato:
	- Logradouro,
	- nro
	- bairro
	- cidade/sigla
	- estado
- Deve ser armazenado somento os números do CPF. não podemos cadastar 2 usuário com o mesmo CPF

### obs:
- Paravincular um usuário a conta, filtre a lista de usuários buscando o número do CPF informando para cada usuário da lista.

## Contribuição

Sinta-se livre para contribuir com este projeto e adicionar novos    recursos ao gerador de senhas.
