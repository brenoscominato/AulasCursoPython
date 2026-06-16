# 1. A fábrica de multiplicadores (Função externa)
def criar_multiplicador(multiplicador):
    # A função interna que lembra do multiplicador
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


# 2. Criando as funções específicas (Os "carimbos")
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

# 3. Testando as funções
print(duplicar(5))       # Saída: 10
print(triplicar(5))      # Saída: 15
print(quadruplicar(5))   # Saída: 20
