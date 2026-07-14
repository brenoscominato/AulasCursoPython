#EXERCICIO DE DICIONÁRIO - JOGO DE PERGUNTA E RESPOSTA
""""
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    resposta_usuario = int(input("Escolha uma opcao: "))
    opcao_escolhida = pergunta['Opções'][resposta_usuario]
    resposta_certa = pergunta['Resposta']
    if opcao_escolhida == resposta_certa:
        print('Você acertou! 🎉')
    else:
        print('Você errou! ❌')
"""
#EXERCICIO DE DICIONARIO - CHAVES E DICIONARIOS INTERNOS
""""
contatos = {
              'Nathalia': {'telefone': '99999-0000', 'email': 'nathalia@email.com', 'sexo': 'F'},
        'Breno': {'telefone': '98888-1111', 'email': 'breno@email.com', 'sexo': 'M'},
}

nome_buscado = input('Digite um dos nomes abaixo:\nBreno\nou\nNathalia\n\n').capitalize()

if nome_buscado in contatos:
    dados_do_contato = contatos[nome_buscado]

    print('\nDados Encontrado: ')
    print(f'Telefone: {dados_do_contato['telefone']}')
    print(f'E-mail: {dados_do_contato['email']}')
    print(f'Sexo: {dados_do_contato['sexo']}')
else:
    print("\nContato não encontrado!")
"""
# EXERCICIO DE DICIONARIO - CONTAGEM DE PALAVRAS E ADICIONANDO NO DICIONARIO
""""
frase = input('Digite uma frase: ')
palavras = frase.split()

quantidade = {}

for palavra in palavras:
    if palavra in quantidade:
        quantidade[palavra] += 1
    else:
        quantidade[palavra] = 1
print(quantidade)
for palavra, contagem in quantidade.items():
    print(f'- "{palavra}": {contagem} vez(es)')

########################################################################################
#MESMO EXERCICIO QUE ACIMA

sabores = input('Digite os sabores das pizzas para a próxima confraternizacao: ')
lista_sabores = sabores.split()

pizzas = {}

for pizza in lista_sabores:
    if pizza in pizzas:
        pizzas[pizza] +=1
    else:
        pizzas[pizza] = 1
print(pizzas)
for pizza, contagem in pizzas.items():
    print(f'- "{pizza}": {contagem} vez(es)')
"""