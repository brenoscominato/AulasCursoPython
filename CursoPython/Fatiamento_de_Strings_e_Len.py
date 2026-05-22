"""
Fatiamento de Strings

 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]

Obs.: a função len retorna a quantidade de caracteres da string
"""

variavel = 'Olá Mundo'
print(variavel[4])
print(variavel[-9])
print(variavel[-7:9])
print(variavel[-9:-6])
print(len(variavel[-9:-6]))
print(variavel[0:9:1])
print(variavel[:-10:-1])