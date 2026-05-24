while True:
    cpf = input('Digite os nove primeiros digitos do seu cpf: ')
    contagem = 10
    lista_contagem = []
    lista_cpf = []

    if len(cpf) !=9:
        print('CPF deve conter 9 digitos')
        continue

    for indice, numero_cpf in enumerate(cpf, start=10):
        lista_cpf.append(numero_cpf)
        lista_contagem.append(contagem)
        contagem -= 1

    print(*lista_contagem)
    print(*lista_cpf)