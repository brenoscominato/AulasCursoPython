numero = input('Digite um numero: ')
recebe_numero = int(numero)

if recebe_numero % 10 == 0:
    print('Múltiplo de 10')
elif recebe_numero % 2 == 0:
    print('Múltiplo de 2')
elif recebe_numero % 5 == 0:
    print('Múltiplo de 5')
else:
    print('Não é múltiplo de 2 nem de 5 ')