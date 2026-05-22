"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número  é par ou impar. Caso o usuário não digite  um número
inteiro, informe que não é um número inteiro

numero = input('Digite um numero inteiro: ')

try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print('Este numero é par')
    elif numero_inteiro % 2 != 0:
        print('Este numero é impar')
except:
     print('Você não digitou um número inteiro')
"""

"""
Faça um programa que pergunte ao usuário e, baseando-se no horário
descrito exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

horario = int(input('Digite um horário: '))

if horario <= 11:
    print('Bom dia')
elif horario <= 17:
    print('Boa tarde')
else:
    print('Boa noite')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva " Seu nome é curto"; se tiver 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')
nome_contado = len(nome)

if nome_contado <= 4:
    print('Seu nome é curto')
elif nome_contado <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
