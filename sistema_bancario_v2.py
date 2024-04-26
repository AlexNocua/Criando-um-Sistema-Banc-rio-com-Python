menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
clientes = []
usuario = {}
contas = []
valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
NUM_AGENCIAS = '0001'

# criar as funcoes pra o saque, deposito e extrato


def saque(*, saldo=saldo, valor=valor, extrato=extrato, limite=limite,
          numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES):
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques


def deposito(valor, saldo, extrato, /):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato


def extrato_view(saldo, /, *, extrato=extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# #criar as funcoes de cadastrar um novo usuario e outra conta do banco


def novo_usuario(nome, data_nacimento, cpf, endereco):
    if cpf in usuario.values():
        return f'\n\n xxxxxxxxxxxxxxx O usuario ja existe com CPF {cpf}, ja existe. xxxxxxxxxxxxxxx'
    else:
        usuario['nome'] = nome
        usuario['data_nacimento'] = data_nacimento
        usuario['cpf'] = cpf
        usuario['endereco'] = endereco
        clientes.append(usuario)
        return f'\n\n xxxxxxxxxxxxxxx O usuario {nome} foi criado como susseso. xxxxxxxxxxxxxxx'


def criar_conta(usuario):
    contas.append({'num_conta': len(contas)+1,
                   'num_agencia': NUM_AGENCIAS,
                   'usuario': usuario})


# logica de movimentos
def logica_movimentos():
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                global saldo, extrato
                saldo, extrato = deposito(valor, saldo, extrato)

            else:
                print("Operação falhou! O valor informado é inválido.")
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            global excedeu_saldo, excedeu_limite, excedeu_saques, LIMITE_SAQUES, numero_saques
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if valor > 0:
                saldo, extrato, numero_saques = saque(saldo, valor, extrato,
                                                      limite, numero_saques, LIMITE_SAQUES)
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            extrato_view(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# logica de contas


def logica_de_contas(usuario):
    while True:
        operação = input(f'''
################################
Seja bem-vindo {usuario}

Por favor seleccione uma das opcoes:

[c] Criar conta
[a] Accesar na Conta
[q] Sair

################################
=>''')
        if operação == 'c':
            criar_conta(usuario)

        elif operação == 'a':
            print('Estas sao as contas que voce tem:\n')
            for i in contas:
                print(i)
            accessar_conta = int(
                input('Digite o numero da conta para accessar: '))
            if contas[accessar_conta-1]['num_conta']:
                logica_movimentos()
        elif operação == "q":
            break
        else:
            print("Operação falhou! O valor informado é inválido.")


#  while para a criacao do usuario.
while True:
    operação = input('''
################################
Por favor seleccione uma das opcoes:

[n] Novo usuario
[a] Accessar como usuario
[q] Sair

################################
=>''')
    print(usuario)
    if operação == 'n':
        nome = input('Digita o nome do usuario:')
        data_nacimento = input('digita a data de nacimento:')
        cpf = int(input('Digita o CPF:'))
        endereco = input(
            'Digita o endereco da seguente forma: lograduro,nro-barrio-cidade/sigla estado:')
        print(novo_usuario(nome, data_nacimento, cpf, endereco))

    elif operação == 'a':
        cpf = int(input('Digite o CPF:'))
        nome = input('Digite o nome:')
        if cpf in usuario.values():
            print('Susseso')
            logica_de_contas(nome)
        else:
            print(f'O usuario com o CPF {cpf} nao existe.')
    elif operação == "q":
        break

    else:
        print("Operação falhou! O valor informado é inválido.")
