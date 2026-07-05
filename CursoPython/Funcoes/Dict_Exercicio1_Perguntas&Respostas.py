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