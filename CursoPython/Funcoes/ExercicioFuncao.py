def multiplica(*args):
    contador = 1
    for numeros in args:
        print('Conta', contador, '*', numeros)
        contador = contador * numeros
        print('Resultado Conta: ', contador)
    return contador
    
numeracao = 1, 7, 9, 10
resultado_real = multiplica(*numeracao)
print(resultado_real)