lista = [
    {'nome': 'Breno', 'sobrenome': 'Cominato'},
    {'nome': 'Nathalia', 'sobrenome': 'Lobato'},
    {'nome': 'Ellie', 'sobrenome': 'Lobato'},
    {'nome': 'Teste', 'sobrenome': 'Silva'},
    {'nome': 'Rato', 'sobrenome': 'Ellie'},
]

#Funcao forma tradicional
#def ordena(item):
#    return item['sobrenome']

#lista.sort(key=ordena)

#Funcao Lambda
lista.sort(key=lambda item: item['nome'])


for item in lista:
    print(item)