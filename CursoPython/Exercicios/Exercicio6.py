''''
#Tabuada

numero = int(input("Digite um número para ver a tabuada: "))
contagem = 0

for i in range(1, 11):
    contagem += 1
    resultado = numero * contagem
    print(f'{numero} x {contagem} = {resultado}')
'''


""""
# Validaçao de Par ou Impar

lista = []
indice = 0

while True:
    while indice < 5:
        try:
            numeros = int(input('Digite um 5 numeros diferentes: '))
            if numeros in lista:
                print('Digite um numero diferente')
            else:
                indice+=1
                lista.append(numeros)
        except:
            print('Digite um numero inteiro')
        print(lista)
    for i in lista:
        if i % 2 == 0:
            print(f'{i} é par')
        else:
            print(f'{i} é impar')
    break
"""

''''
# Maior ou Menos

lista = []
indice = 0

while True:
    while indice < 5:
        try:
            numeros = int(input('Digite um 5 numeros diferentes: '))
            if numeros in lista:
                print('Digite um numero diferente')
            else:
                indice+=1
                lista.append(numeros)
        except:
            print('Digite um numero inteiro')
        print(lista)
    menor = lista[0]
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    print(maior)
    print(menor)
    break
'''
""""
#Numeros primos

numero = int(input("Digite um numero: "))
divisoes = 2
primo = True

while True:
    while divisoes < numero:
        if numero % divisoes == 0:
            primo = False
        divisoes+=1
    print(primo)
    break
"""

""""
#contador de letras

contaespaco = 0

while True:
    frase = str(input('Digite uma frase: '))
    for i in frase:
        if i == " ":
            contaespaco+=1
    break
print(f'Na frase tem {contaespaco} espaços')
print(f'Na frase tem {contaespaco + 1} palavras')
"""

contador = 0

while True:
    meu_nome = str(input('Digite seu nome: '))
    for letra in meu_nome:
        print(letra)
        if letra != ' ':
            contador+=1
        else:
            continue
    break
print(contador)

    



