''''
#Tabuada

numero = int(input("Digite um número para ver a tabuada: "))
contagem = 0

for i in range(1, 11):
    contagem += 1
    resultado = numero * contagem
    print(f'{numero} x {contagem} = {resultado}')
'''

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