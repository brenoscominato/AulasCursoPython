""""
Valores padrao para parâmetros
Ao definir uma funcao, os parametros podem
ter valores padrao. Caso o valor nao seja enviado
para o parametro, o valor será usado.
Refatorar: Editar o seu codigo
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 9)
soma(4, 7)
soma(3, 4, 1)