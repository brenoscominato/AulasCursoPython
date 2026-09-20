numero = input('Digite um numero: ')
recebe_numero = int(numero)


try:
    if recebe_numero > 0:
        print('POSITIVO')
    elif recebe_numero < 0:
        print('NEGATIVO')
except:
    print('NULO')