#Dicionario é um conjunto não ordenado de pares chave : valor. São delimitados por chaves, podendo ser mútavel e imutável.
#ex:
pessoa = {
    'nome': 'João' , 'idade':18  
} 
print(pessoa)

#Para acessarmos os valores, faremos igual nos dicionários 

print(pessoa['nome'])

# Caso a gente queira mudar os valores que a chave possui, faremos das mesma forma, adicionando apenas um sinal de atribuição.

pessoa['nome'] = 'Pedro'

print(pessoa)

pessoa = {
    'nome':{'nome': 'João' , 'idade': 18} ,
    'nome2': {'nome':'Maira', 'idade': 10},
    'nome3': {'nome':'Julia', 'idade' : 18}
} 

# Caso a gente tenha uma lista muito grande, e queremos imprimir ela para o usuário, podemos por ela dentro de um FOR, usando a função ITEMS()

for chave, valor in pessoa.items():
    print(chave, valor)
    
    
#Como adicionar uma nova chave no nosso dicionário:

pessoa['Maria Julia '] = {'nome': 'Mj', 'idade': 18}  #No dicionário que queremos adicionar um novo valor, colocamos entre colochetes a chave que queremos e entre chaves, adicionamos os outros valores.

print(pessoa)