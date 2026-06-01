#O que são funçoes?
#É um bloco de código que ultilizamos para não precisarmos escrever um certo código várias vezes.
# Pode receber parâmetros e retornar valores 

def ola(): #Não informamos nenhum parâmetro.
    print('Olá mundo')
    
ola()  


def ola2(nome):  #tem que receber o parâmetro nome
    print(f'Olá, {nome}!')
    
ola2('João') #Informamos o parâmetro

def ola3(nome = 'Anonimo'):  #tem que receber o parâmetro nome, caso o usuário não informe o nome, o nome será automaticamente "Anonimo" e não dará o erro.
    print(f'Olá, {nome}!')
    
ola2('João')