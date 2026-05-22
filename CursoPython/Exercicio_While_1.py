#Exercicio 1
"""

nome = 'Breno Silva Cominato'

tamanho_nome = len(nome)
nome_inicio = 0
nome_concatenado = ''


while nome_inicio < tamanho_nome:
    nome_concatenado += '*' + nome[nome_inicio]
    nome_inicio += 1

print(nome_concatenado)
"""
#Exercicio 2
"""
nome = 'Breno Silva'

tamanho_nome = len(nome)
nome_inicio = 0
nome_concatenado = ''


while nome_inicio < tamanho_nome:
    nome_concatenado += '-' + nome[nome_inicio]
    nome_inicio += 1

print(nome_concatenado)
"""
#Exercicio 3

"""
nome = 'Breno Cominato'

nome_inicio = 0
contador = 0

while True:
    try:
        nome[nome_inicio]
        contador += 1
        nome_inicio += 1
    except IndexError:
        break

print(contador)
"""
#Exercicio 4
"""
numero = 0

while numero <= 10:
    print(f'Este aqui é o numero {numero}')
    numero += 1

print('Este aqui é o meu teste')
"""
#Exercicio 5

"""
nome = 'Breno Silva Cominato'

nome_atual = 0

while True:
        try:
            nome[nome_atual]
            print(nome[nome_atual])
            nome_atual += 1
        except IndexError:
              break
"""

#Exercicio 6

""""
nome = 'Breno'
contato = int(len(nome))
i = contato - 1
linha = ''

while i >= 0:
        linha = nome[i]
        i -= 1
        print(linha + i)
"""
#Exercicio 7
"""
nota = float(input("Digite uma nota entre zero e 10: "))

while nota > 10 or nota < 0:
    nota = float(input("Informe um valor válido: "))
"""

#Exercicio 8

usuario = input('Usuário: ')
senha = input('Senha : ')

while senha == usuario:
    print('A senha não pode ser igual ao usuário')
    usuario = input('Usuário: ')
    senha = input('Senha: ')