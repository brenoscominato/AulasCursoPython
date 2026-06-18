#FUNCAO QUE VALIDA UM USUARIO E SENHA
# def logins(nome_usuario, senha_usuario):

#     def login(usuario):
#         if usuario == senha_usuario:
#             return f'Usuário {nome_usuario} logado com sucesso!!'
#         return f'Acesso negado para o usuário {nome_usuario}'
#     return login

# user1 = logins('Breno', 1234)
# user2 = logins('Nathalia', 123456)

# print(user1(1234))    # Retorna: Usuário Logado
# print(user2(121111))  # Retorna: Usuário Logado

#FUNCAO QUE VALIDA A SOMA DE DOIS VALORES E MOSTRA O NOME DO USUARIO
# def adicao(nome, numeracao):
#     def conta(numero):
#         return f'{nome} sua conta foi de {numero + numeracao} reais'
#     return conta
    
# conta1 = adicao('Breno', 4)
# conta2 = adicao('Nathalia', 10)

# print(conta1(23))
# print(conta2(18))

def informacoes_pessoais(nome, idade, sexo):
    def pessoa():
        return f'Seu nome é {nome}, você tem {idade} anos de idade e é do sexo {sexo}'
    return pessoa


pessoa1 = informacoes_pessoais('Breno', 28, 'Masculino')
pessoa2 = informacoes_pessoais('Nathalia', 29, 'Feminino')

print(pessoa1())
print(pessoa2())