# Sistema Bancário em Python

Projeto desenvolvido como desafio prático durante meus estudos de Python.

O objetivo é implementar uma versão simples de um sistema bancário utilizando conceitos fundamentais da linguagem, como variáveis, estruturas condicionais, estruturas de repetição, tratamento de exceções e manipulação de strings.

## Funcionalidades

O sistema possui quatro opções principais:

- Depositar valores
- Realizar saques
- Visualizar o extrato
- Encerrar o sistema

## Regras de negócio

### Depósito

- Apenas valores positivos são aceitos
- O saldo é atualizado após cada depósito
- Todos os depósitos são registrados no extrato
- Entradas não numéricas são tratadas sem encerrar o programa

### Saque

- O valor do saque deve ser positivo
- O usuário não pode sacar um valor maior que o saldo disponível
- Cada saque possui limite máximo de **R$ 500,00**
- São permitidos no máximo **3 saques**
- Todos os saques realizados são registrados no extrato
- Entradas não numéricas são tratadas sem encerrar o programa

### Extrato

O extrato exibe:

- Todos os depósitos realizados
- Todos os saques realizados
- Saldo atual da conta

Caso nenhuma movimentação tenha sido realizada, o sistema informa que não existem movimentações.

## Exemplo do menu

```text
Qual operação você deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>