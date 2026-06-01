# *args meio que transforma a variável que está dos do * em uma tupla, fazendo com que a gente consiga realizar calculos e mais coisas com a tupla.

def nsei(*args):    # a gente pode colocar outros nomes no lugar de args, o que importa é o *
    return print(sum(args))

nsei(1,5,6,8,7,2,6)

#E o **kwargs o usuário pode inserir um dado e o valor do dado, ou seja, é um dicionário que possui chave e valor.

def cadastros(nome, **kwargs):
    
    print(f'Olá, {nome}!')
    
    for chave, valor in kwargs.items():
        print(f'{chave} {valor}')
        
telefone = 63992687993
cidade = 'Aux'

cadastros('João', tel = telefone, cidade = cidade, hobbie = 'Jogar')  #Aqui irá receber os valores na ordem que foi colocado na função.
