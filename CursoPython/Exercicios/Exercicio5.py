#Solicita o nome e idade, e mostra na tela
""""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print(f'Olá, {nome}! Você tem {idade} anos')
"""

#Solicita um numero e mostra o dobro dele
""""
numero = input('Digite um numero: ')
recebe_numero = int(numero)
dobro = recebe_numero * 2

print(f'{dobro} é o dobro do numero que digitou')
"""

#Converte graus Celcius em Fahrenheit
"""
celcius = input('Digite a temperatura em Celcius: ')
recebe_celcius = int(celcius)
temp_fahrenheit = (recebe_celcius * 1.8) + 32

print(f'Você digitou {celcius} graus de temperatura em celcius, que equivalem a {temp_fahrenheit:.0f} graus em Fahrenheit')

"""

#Verifica se o numero é par ou impar
"""
numero = int(input('Digite um numeto: '))
divisivel = numero % 2 == 0

if divisivel:
    print('Este numero é PAR')
else:
    print('Este numero é IMPAR')
"""

#Verifica qual dentre dois numetos é maior, menor ou se são iguais
"""
numero1 = int(input('Digite um número: '))
numero2  = int(input('Digite outro número: '))

if numero1 > numero2:
    print('O primeiro digitado numero é maior! ')
elif numero1 < numero2:
    print('O segundo numero digitado é maior! ')
else:
    print('Os números são iguais! ')
"""

#Aprovação de alunos
"""
nota = int(input('Digite a nota do aluno: '))

if nota >= 7:
    print('Aluno Aprovado! ')
elif nota >= 5:
    print('Aluno em Recuperação! ')
elif nota <= 5:
    print('Aluno reprovado! ')
"""

#Calculadora de numeros
"""
#Versao 1
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
operacao = input('Digite algumas dos operadores a seguir (+, -, *, /)')
adicao = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

if operacao == '+':
    print(f'A soma dos números digitados é {adicao}')
elif operacao == '-':
    print(f'A subtracao dos números digitados é {subtracao}')
elif operacao == '*':
    print(f'A multiplicação dos números digitados é {multiplicacao}')
elif operacao == '/':
    print(f'A divisão dos números digitados é {divisao:.0f}')
else:
    print('Você não digitou um operador correspondente')

#Versao 2
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
operacao = input('Digite um operador (+, -, *, /): ')

if operacao == '+':
    print(f'Resultado: {numero_1 + numero_2}')
elif operacao == '-':
    print(f'Resultado: {numero_1 - numero_2}')
elif operacao == '*':
    print(f'Resultado: {numero_1 * numero_2}')
elif operacao == '/':
    if numero_2 == 0:
        print('Erro: divisão por zero!')
    else:
        print(f'Resultado: {numero_1 / numero_2:.2f}')
else:
    print('Operador inválido!')
"""

#Classificação de idade

"""
idade = int(input('Digite uma idade: '))

if idade <=12 :
    print(f'Você digitou {idade}, logo é uma criança')
elif idade <= 17:
    print(f'Você digitou {idade}, logo é um adoslecente')
elif idade >=59:
    print(f'Você digitou {idade}, logo é um adulto')
else:
    print('Nao digitou uma idade correspondente')
"""

#Simulador de login

"""
Versao 1
usuario_correto = str('admin')
senha_correta = int('1234')
usuario = str(input('Digite o Login: '))
senha = int(input('Digite a senha: '))

if usuario == usuario_correto and senha == senha_correta:
    print('Usuário logado com sucesso!!')
else:
    print('Acesso Negado, verifique o login e senha e tente novamente.')

#Versao 2
usuario_correto = 'admin'
senha_correta = '1234'
usuario = (input('Digite o Login: '))
senha = (input('Digite a senha: '))

if usuario == usuario_correto:
    if senha == senha_correta:
        print('Login realizado com sucesso!')
    else:
        print('Senha incorreta!')
else:
    print('Usuário não encontrado!')
"""

#Descontro Progressivo

"""
compra = float(input('Digite o valor da compra: '))
desconto_1 = float(0.10 * compra)
desconto_2 = float(0.20 * compra)

if compra <= 100:
    print('Desconto não aplicado para compras de até 100.00 reais')
elif compra <= 200:
    print(f'Seu desconto foi de 10%, logo sua compra saiu por R${compra - desconto_1:.2f}')
else:
    print(f'Seu desconto foi de 20%, logo sua compra saiu por R${compra - desconto_2:.2f}')
"""