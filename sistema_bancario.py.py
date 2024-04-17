menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

# criacao das variaveis

saldo = 0
saque = 0
deposito = 0
limite = 500
extrato = ''
numero_saques = 0  # lembrar que o maximo é treis
LIMITE_SAQUES = 3

while True:
    print(menu)

    opcao = int(input())
    if opcao == 1:
        print('Deposito')
        deposito = int(input('Digite o que deseja depositar\n'))
        if deposito <= 0:
            print('nao é possivel fazer o deposito.')
        else:
            saldo += deposito
            extrato += f'Fiz um deposito de R$ {deposito:.2f}\n'
    elif opcao == 2:
        if numero_saques == LIMITE_SAQUES:
            print('O numero maximo de saques sao 3, Tente de novo o dia que vem')
            print(extrato)
        else:
            print('Sacar')
            saque = int(input('Quanto deseja ter de saque?\n'))
            if saque > saldo or saque > limite:
                print('nao é possivel fazer o saque.')
            else:
                numero_saques += 1
                saldo -= saque
                extrato += f'Fiz um saque de R$- {saque:.2f}\n'
                print('Sucesso')
    elif opcao == 3:
        print('''
##############################################################
              Nao foram realizadas movimentacoes
##############################################################'''
              if not extrato else extrato)
        
    elif opcao == 4:
        break
    else:
        print('Operacao invalida, por favor selecione novamente a operacao desejada')
