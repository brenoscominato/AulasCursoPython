pessoa = {
    'nome': 'Breno',
    'sobrenome': 'Cominato',
    'idade': '28',
    'sexo': 'Masculino',
    'empresa': 'Shift',
    'endereco': [
        {'rua': 'Rua Santina Ferreira Cruz', 'numero': '1234'},
        {'rua': 'Rua Santina Ferreira Cruz', 'numero': '1234', 'complemento': 'Apto 13'},
    ],
}

for i in pessoa:
    print(i, pessoa[i])

print()

print(pessoa['nome'])