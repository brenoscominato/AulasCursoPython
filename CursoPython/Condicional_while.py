"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

"""
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')

"""

"""
contador = 11


while contador > 0:
    contador -= 1
    print(contador)
    
print('A contagem regressiva acabou')
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')
