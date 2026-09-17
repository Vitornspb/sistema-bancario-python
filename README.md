# Sistema Bancário em Python

Projeto desenvolvido como desafio prático durante meus estudos de Python.

O objetivo é construir um sistema bancário simples aplicando conceitos fundamentais da linguagem e evoluindo o projeto de forma incremental.

Nesta segunda versão, o sistema foi modularizado em funções e passou a permitir o cadastro de usuários e contas bancárias.

## Funcionalidades

O sistema possui as seguintes operações:

- Depositar valores
- Realizar saques
- Visualizar o extrato
- Cadastrar novos usuários
- Criar novas contas bancárias
- Listar contas cadastradas
- Encerrar o sistema

## Regras de negócio

### Depósito

- Apenas valores positivos são aceitos
- O saldo é atualizado após cada depósito
- Todos os depósitos são registrados no extrato
- Entradas não numéricas são tratadas sem encerrar o programa
- A operação de depósito foi separada em uma função
- A função recebe seus argumentos apenas por posição

### Saque

- O valor do saque deve ser positivo
- O usuário não pode sacar um valor maior que o saldo disponível
- Cada saque possui limite máximo de **R$ 500,00**
- São permitidos no máximo **3 saques**
- Todos os saques realizados são registrados no extrato
- Entradas não numéricas são tratadas sem encerrar o programa
- A operação de saque foi separada em uma função
- A função recebe seus argumentos apenas por nome

### Extrato

O extrato exibe:

- Todos os depósitos realizados
- Todos os saques realizados
- Saldo atual da conta

Caso nenhuma movimentação tenha sido realizada, o sistema informa que não existem movimentações.

A função de extrato utiliza:

- `saldo` como argumento posicional
- `extrato` como argumento nomeado

### Cadastro de usuários

Cada usuário possui:

- Nome
- Data de nascimento
- CPF
- Endereço

Regras:

- Os usuários são armazenados em uma lista
- O CPF é utilizado para identificar o usuário
- Não é permitido cadastrar dois usuários com o mesmo CPF
- O CPF deve ser armazenado apenas com números

### Contas bancárias

Cada conta possui:

- Agência
- Número da conta
- Usuário vinculado

Regras:

- A agência é fixa: `0001`
- O número da conta é sequencial, iniciando em `1`
- Um usuário pode possuir mais de uma conta
- Cada conta pertence a apenas um usuário
- As contas são armazenadas em uma lista

## Exemplo do menu

```text
Qual operação você deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=>
```

## Conceitos praticados

Durante o desenvolvimento foram utilizados:

- Variáveis e constantes
- Tipos de dados
- Operadores
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Dicionários
- Funções
- Argumentos posicionais
- Argumentos nomeados
- `positional only`
- `keyword only`
- Tratamento de exceções com `try` e `except`
- Manipulação de strings
- Formatação com f-strings
- Modularização de código

## Tecnologias utilizadas

- Python
- Git
- GitHub

## Estrutura do projeto

```text
sistema-bancario-python/
│
├── main.py
├── README.md
└── .gitignore
```

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd sistema-bancario-python
```

Execute:

```bash
python main.py
```

No Windows, também pode utilizar:

```bash
py main.py
```

## Evolução do projeto

### Versão 1

Implementação das operações básicas:

- Depósito
- Saque
- Extrato

### Versão 2

Evolução do sistema com:

- Modularização das operações em funções
- Cadastro de usuários
- Cadastro de contas
- Vinculação entre conta e usuário
- Listagem de contas
- Uso de argumentos posicionais e nomeados

## Objetivo do projeto

Este projeto faz parte do meu processo de aprendizado em Python, com foco na aplicação prática dos fundamentos da linguagem e na evolução gradual para códigos mais organizados, modulares e reutilizáveis.