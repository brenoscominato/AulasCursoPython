# # Desempacotamento em chamadas
# # de métodos e funções
# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'
# salas = [
#     # 0        1
#     ['Maria', 'Helena', ],  # 0
#     # 0
#     ['Elaine', ],  # 1
#     # 0       1       2
#     ['Luiz', 'João', 'Eduarda', ],  # 2
# ]

# # p, b, *_, ap, u = lista
# # print(p, u, ap)

# # print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# # print(*lista)
# # print(*string)
# # print(*tupla)

# print(*salas, sep='\n')


ListaTeste = ['Breno', 'Nathalia', 'Ellie', 1,2,3,4]
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

a, b, c, *_, d = ListaTeste

print(*_)
print(*ListaTeste)
print(*salas, sep='\n')