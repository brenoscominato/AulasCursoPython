"""
Higher Order Functions
Funções de primeira classe
"""


# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'


# def executa(funcao, *args):
#     return funcao(*args)


# print(
#     executa(saudacao, 'Bom dia', 'Luiz')
# )
# print(
#     executa(saudacao, 'Boa noite', 'Maria')
# )

def nome(primeiro, segundo, terceiro):
    return f'{primeiro} {segundo} {terceiro}'

def executa(funcao, *args):
    return funcao(*args)


print(executa(nome, 'Breno', 'Silva', 'Cominato'))