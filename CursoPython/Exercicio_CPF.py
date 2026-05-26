while True:
    cpf = input('Digite os nove primeiros digitos do seu cpf: ')
    contagem = 10
    lista_contagem = []
    lista_cpf = []
    resultado_multiplicacao = 0

    if len(cpf) !=9:
        print('CPF deve conter 9 digitos')
        continue

    for indice, numero_cpf in enumerate(cpf, start=10):
        lista_cpf.append(numero_cpf)
        lista_contagem.append(contagem)
        contagem -= 1

    for lista_contada, lista_cpf_contada in zip(lista_contagem, lista_cpf):
        #print(f'{lista_contada} x {lista_cpf_contada}')
        resultado_multiplicacao += lista_contada * int(lista_cpf_contada)

    if resultado_multiplicacao % 11 < 2:
        print('O primeiro digito verificador é: 0')
    else:
        print(f'O primeiro digito verificador é: {11 - (resultado_multiplicacao % 11)}')

    for indice, numero_cpf in enumerate(cpf, start=11):
        lista_cpf.append(numero_cpf)
        lista_contagem.append(contagem)
        contagem -= 1
    
    for lista_contada, lista_cpf_contada in zip(lista_contagem, lista_cpf):
        #print(f'{lista_contada} x {lista_cpf_contada}')
        resultado_multiplicacao += lista_contada * int(lista_cpf_contada)

    if resultado_multiplicacao % 11 < 2:
        print('O segundo digito verificador é: 0')
    else:
        print(f'O segundo digito verificador é: {11 - (resultado_multiplicacao % 11)}')

    # print(*lista_contagem)
    # print(*lista_cpf)
    print(f'Resultado da multiplicação: {resultado_multiplicacao}')
    break