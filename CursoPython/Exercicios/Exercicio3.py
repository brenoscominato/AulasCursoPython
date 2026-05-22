salaro = input('Digite seu salario: ')
prestacao = input('Digite o valor da prestacao: ')
recebe_salaro = int(salaro)
recebe_prestacao = int(prestacao)

if recebe_prestacao <= (0.3 * recebe_salaro):
    print('Emprestimo concedido')
else:
    print('Emprestimo não concedido')
