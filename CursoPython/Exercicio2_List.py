import os

lista = []

while True:
        print("Selecione uma opcao: ")
        opcao = input("[i]nserir [a]pagar [l]istar: ")
        if opcao == 'i':
            valor = input('Alimento: ')
            lista.append(valor)
        elif opcao == 'a':
            indice_str = input('Digite o indice que deseja apagar: ')
            try:
                indice  = int(indice_str)
                del lista[indice]
            except:
             print("Nao há dados para excluir")
        elif opcao == 'l':
            for i, lista_compra in enumerate(lista):
                print(f"{i} {lista_compra}")