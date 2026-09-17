menu = """

Qual operação você deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=> """

AGENCIA = "0001"
LIMITE_SAQUE = 500
LIMITE_SAQUES = 3


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        print(
            f"Depósito de R$ {valor:.2f} realizado com sucesso! "
            f"Saldo atual: R$ {saldo:.2f}"
        )

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(
    *,
    saldo,
    valor,
    extrato,
    limite,
    numero_saques,
    limite_saques
):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)

    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")


def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

    return None


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario_existente = buscar_usuario(cpf, usuarios)

    if usuario_existente:
        print("Já existe um usuário cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input(
        "Informe a data de nascimento (dd/mm/aaaa): "
    ).strip()

    endereco = input(
        "Informe o endereço "
        "(logradouro, nro - bairro - cidade/UF): "
    ).strip()

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()

    usuario = buscar_usuario(cpf, usuarios)

    if usuario is None:
        print(
            "Usuário não encontrado. "
            "Cadastre o usuário antes de criar uma conta."
        )
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    print("Conta criada com sucesso!")

    return conta


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n================ CONTAS ================")

    for conta in contas:
        print(
            f"Agência: {conta['agencia']} | "
            f"Conta: {conta['numero_conta']} | "
            f"Titular: {conta['usuario']['nome']} | "
            f"CPF: {conta['usuario']['cpf']}"
        )

    print("=========================================")


saldo = 0
extrato = ""
numero_saques = 0
usuarios = []
contas = []


while True:

    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(
                input("Informe o valor do depósito: ")
            )

        except ValueError:
            print(
                "Operação falhou! "
                "Informe um valor numérico válido."
            )
            continue

        saldo, extrato = depositar(
            saldo,
            valor,
            extrato
        )

    elif opcao == "s":

        print(f"Saldo atual: R$ {saldo:.2f}")

        try:
            valor = float(
                input("Informe o valor do saque: ")
            )

        except ValueError:
            print(
                "Operação falhou! "
                "Informe um valor numérico válido."
            )
            continue

        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=LIMITE_SAQUE,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":

        exibir_extrato(
            saldo,
            extrato=extrato
        )

    elif opcao == "nu":

        criar_usuario(usuarios)

    elif opcao == "nc":

        numero_conta = len(contas) + 1

        conta = criar_conta(
            AGENCIA,
            numero_conta,
            usuarios
        )

        if conta:
            contas.append(conta)

    elif opcao == "lc":

        listar_contas(contas)

    elif opcao == "q":

        print(
            "Saindo do sistema. "
            "Obrigado por utilizar nosso serviço!"
        )
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente "
            "a operação desejada."
        )