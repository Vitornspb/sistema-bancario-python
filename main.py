menu = """

Qual operação você deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0

LIMITE_SAQUE = 500
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(
                f"Depósito de R$ {valor:.2f} realizado com sucesso! "
                f"Saldo atual: R$ {saldo:.2f}"
            )
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        print(f"Saldo atual: R$ {saldo:.2f}")

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")

        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(
                f"Saque de R$ {valor:.2f} realizado com sucesso! "
                f"Saldo atual: R$ {saldo:.2f}"
            )
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo do sistema. Obrigado por utilizar nosso serviço!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")