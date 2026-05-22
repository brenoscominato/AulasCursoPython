"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [at]ualizar:  ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)


    elif opcao == 'at':
        indice_str_at = input(
            'Escolha o índice para atualizar: '
        )
        
        if len(lista) == 0:
            print('Nada para atualizar')
            continue
        valor = input('Valor: ')
        try:
            indice = int(indice_str_at)
            lista[indice] = valor
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    else:
        print('Por favor, escolha i, a , l ou at')