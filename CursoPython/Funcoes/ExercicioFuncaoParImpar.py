
def numero():
    numero = int(input('Digite um numero acima ou igual a 0: '))
    if numero >= 0:
        if numero % 2 == 0:
            return print(f'O número {numero} é par')
        else:
            return print(f'O número{numero} é impar')
    else:
        print('O numero precisa ser maior ou igual a 0')
    return(numero)

numero()