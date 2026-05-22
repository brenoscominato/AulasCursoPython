palavra = 'Arthur'
letras_acertadas = ''
repeticoes = 0

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    repeticoes += 1

    if letra in palavra:
        letras_acertadas += letra

    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra:
        print('Você ganhou!')
        print(f'Tentativas: {repeticoes}')
        break