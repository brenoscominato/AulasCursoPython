#Saldo inicial
import time

saldo_inicial = float(1000)


while True:
    operacao = input(
        '\nMenu\n'
        '1 - Ver saldo\n'
        '2 - Depositar\n'
        '3 - Sacar\n' \
        '4 - Transferir\n'
        '5 - Sair\n\n'
        'Digite a operação desejada: '
    )
    if operacao == '1':
        print(f'Seu saldo atual é: R${saldo_inicial:.2f}')
    elif operacao == '2':
        valor_deposito = float(input(('Digite o valor que deseja depositar: ')))
        if valor_deposito <= 0:
            print('Valor inválido')
        else:
            saldo_inicial = saldo_inicial + valor_deposito
            print(f'Seu novo saldo é de: R${saldo_inicial:.2f}')
    elif operacao == '3':
        valor_sacado = float(input(('Digite o valor que deseja sacar: ')))
        if valor_sacado > saldo_inicial:
            print('O valor do saque não pode ser maior que o seu saldo atual')
        elif valor_sacado <= 0:
            print('Este valor é inválido')
        else:
            saldo_inicial = saldo_inicial - valor_sacado
            print(f'O seu saldo atual é de {saldo_inicial:.2f}')
    elif operacao == '4':
        while True:
            transferencia = input(
            '\nMenu\n'
            '1 - PIX\n'
            '2 - TED\n'
            'Digite a operação desejada: ')
            if transferencia == '1':
                cpf = input('Digite o número do CPF que deve receber a transferência: ')
                cpf = str(cpf).replace(".", "").replace("-", "")
                if len(cpf) == 11:
                    valor_transferido = float(input(('Digite o valor que deseja transferir: ')))
                    print('Iniciando Transferencia')
                    time.sleep(4)#Aguarda 4 segundos
                    print('Transferencia realizada com sucesso!!')
                    saldo_inicial = saldo_inicial - valor_transferido
                    break
                else:
                    print("Erro: O CPF deve conter 11 números.")
            elif transferencia == '2':
                print('Transferencia de TED em manutenção, por gentileza escolha outro método de transferência.')
            else:
                print('Opção inválida')
                break 
    elif operacao == '5':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida')
"""
saldo = 1000.0

while True:
    operacao = input(
        '\nMenu\n'
        '1 - Ver saldo\n'
        '2 - Depositar\n'
        '3 - Sacar\n'
        '4 - Sair\n'
        'Digite a operação desejada: '
    )

    if operacao == '1':
        print(f'Seu saldo atual é: R${saldo:.2f}')

    elif operacao == '2':
        valor = float(input('Digite o valor para depósito: '))

        if valor <= 0:
            print('Valor inválido')
        else:
            saldo += valor
            print(f'Saldo atualizado: R${saldo:.2f}')

    elif operacao == '3':
        valor = float(input('Digite o valor para saque: '))

        if valor <= 0:
            print('Valor inválido')
        elif valor > saldo:
            print('Saldo insuficiente')
        else:
            saldo -= valor
            print(f'Saldo atualizado: R${saldo:.2f}')

    elif operacao == '4':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida')
"""