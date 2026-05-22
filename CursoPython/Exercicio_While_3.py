nome = 'Breno Silva Cominatoo'

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < len(nome):
    letra_atual = nome[i]

    if letra_atual == '':
        i += 1
        continue
    quantidade_atual = nome.count(letra_atual)

    if qtd_mais_vezes <= quantidade_atual:
        qtd_mais_vezes = quantidade_atual
        letra_mais_vezes = letra_atual

    i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_vezes}" que apareceu '
    f'{qtd_mais_vezes}x')