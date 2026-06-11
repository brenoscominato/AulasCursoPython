# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


# def nome():
#     return 'Breno'

# print(nome() + ' Silva Cominato')

# def saudacao(nome, sobrenome = 'Silva'):
#     print(f'Olá, {nome}. Seu sobrenome é {sobrenome}')

# saudacao('Breno', 'Cominato')
# saudacao('Breno')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 9)
multiplo_de(15, 3)
multiplo_de(10, 2)