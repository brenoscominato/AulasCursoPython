while True:
    cpf = input('Digite os 11 dígitos do seu CPF: ')
    contagem = 10
    lista_contagem = []
    lista_cpf = []
    resultado_multiplicacao = 0

    if len(cpf) != 11:
        print('CPF deve conter 11 dígitos')
        continue
    
    # Separa os 9 dígitos e os 2 dígitos verificadores informados
    cpf_numeros = cpf[:9]
    primeiro_digito_informado = int(cpf[9])
    segundo_digito_informado = int(cpf[10])

    for indice, numero_cpf in enumerate(cpf_numeros, start=10):
        lista_cpf.append(numero_cpf)
        lista_contagem.append(contagem)
        contagem -= 1

    for lista_contada, lista_cpf_contada in zip(lista_contagem, lista_cpf):
        #print(f'{lista_contada} x {lista_cpf_contada}')
        resultado_multiplicacao += lista_contada * int(lista_cpf_contada)

    if resultado_multiplicacao % 11 < 2:
        primeiro_digito = 0
        print('O primeiro digito verificador é: 0')
    else:
        primeiro_digito = 11 - (resultado_multiplicacao % 11)
        print(f'O primeiro digito verificador é: {primeiro_digito}')

    resultado_multiplicacao = 0
    contagem = 11
    lista_contagem = []
    lista_cpf = []

    # Inclui os 9 dígitos + o primeiro dígito verificador
    cpf_com_primeiro_digito = cpf_numeros + str(primeiro_digito)
    
    for indice, numero_cpf in enumerate(cpf_com_primeiro_digito):
        lista_cpf.append(numero_cpf)
        lista_contagem.append(contagem)
        contagem -= 1
    
    for lista_contada, lista_cpf_contada in zip(lista_contagem, lista_cpf):
        #print(f'{lista_contada} x {lista_cpf_contada}')
        resultado_multiplicacao += lista_contada * int(lista_cpf_contada)

    if resultado_multiplicacao % 11 < 2:
        segundo_digito = 0
        print('O segundo digito verificador é: 0')
    else:
        segundo_digito = 11 - (resultado_multiplicacao % 11)
        print(f'O segundo digito verificador é: {segundo_digito}')

    # Validação do CPF
    print(f'\n--- Validação ---')
    print(f'Seu CPF completo é: {cpf}')
    print(f'Dígitos informados: {primeiro_digito_informado} e {segundo_digito_informado}')
    print(f'Dígitos calculados: {primeiro_digito} e {segundo_digito}')
    
    if primeiro_digito == primeiro_digito_informado and segundo_digito == segundo_digito_informado:
        print('✓ CPF VÁLIDO!')
    else:
        print('✗ CPF INVÁLIDO!')
    
    break