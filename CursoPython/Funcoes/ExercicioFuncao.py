""""
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
"""

def multiplicacao(numero):
    divisiveis_por_dois = numero % 2 == 0

    if divisiveis_por_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(multiplicacao(3))
print(multiplicacao(40))
print(multiplicacao(37))
print(multiplicacao(355))
print(multiplicacao(6))

