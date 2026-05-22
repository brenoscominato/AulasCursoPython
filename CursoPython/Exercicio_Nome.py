"""
 01234
 Breno
-54321
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
interpolacao = 'Seu nome é %s' % (nome)

if nome and idade:
    print(interpolacao)
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')