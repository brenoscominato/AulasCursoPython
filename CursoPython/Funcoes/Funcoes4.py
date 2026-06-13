""""
Escopo de funcoes em Python
Escopo significa o local em que o codigo pode atingir
Existe o escopo global e o local
O escopo global é o escopo onde todo o código é alcancavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser atingidos
"""


x = 1

def escopo():
    #global x
    x= 10
    def outra_funcao():
        #global x
        x = 11
        y = 2
        print(x , y)
        def nova_funcao(nome, sobrenome):
            print(f'Seu nome é {nome} e seu sobrenome é {sobrenome}')
            
            def multiplica(x, y, z=None):
                if z is not None:
                    print(f'{x=} {y=} {z=}', x * y * z)
                else:
                    print(f'{x=} {y=}', x * y)
            multiplica(3, 3)
            multiplica(2, 2, 1)
        nova_funcao(nome='Breno', sobrenome='Cominato')
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)