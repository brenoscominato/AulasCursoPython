

def soma (*args):
    total = 0
    for numero in args:
        print('Conta', total, '+', numero)
        total = total + numero
        print('Resultado', total)
    print(total)


soma(1,2,3,4,5,6)