""""
Argumentos nomeados e não nomeados em funcoes Phyton
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f'{x=} y={y}' '|', 'x + y = ', x + y)

soma(1, 2)
soma(y=2, x=1)