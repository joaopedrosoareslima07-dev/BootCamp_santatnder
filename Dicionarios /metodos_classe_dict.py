pessoa = {
    'nome':{'nome': 'João' , 'idade': 18} ,
    'nome2': {'nome':'Maira', 'idade': 10},
    'nome3': {'nome':'Julia', 'idade' : 18},
    'Dalvani':{'nome': 'Dalvani', 'idade': 37}
} 

for chave, valor in pessoa.items():
    print(chave, valor)
    
    
#Metodo clear -- Irá apagar tudo da lista
pessoa.clear()
print(pessoa)

#Méttodo copy() ---Irá copiar a lista

copia = pessoa.copy() #Criou uma segunda variável que contem todos os valores do dicionário, podendo modifica-los sem alterar o valor dela original 


#Fromkeys() -- Cria chave pra você, sem valores. A segunda situação é quando criamos as chaves que queremso que os valores sejam iguais.

naoSei = dict.fromkeys(['nome', 'idade'])  #Esse método retorna as chaves com os valores NONE 
print(naoSei)

naoSei = dict.fromkeys(['nome', 'idade'], 'Vazio')  #Esse método retorna as chaves com os valores VAZIO
print(naoSei)
 
 
pessoa = {
    'nome':{'nome': 'João' , 'idade': 18} ,
    'nome2': {'nome':'Maira', 'idade': 10},
    'nome3': {'nome':'Julia', 'idade' : 18},
    'Dalvani':{'nome': 'Dalvani', 'idade': 37}
} 

 
 #Método get()   é uma segunda forma de acessar os valores de um dicionário
 
print()
print(pessoa.get('Dalvani')) #Puxa as chaves e valores de Dalvani

#Caso você passe uma chave que não existe no dicionário, ele retorna com o valor NONE. No método get é possivel mudar esse retorno, 

print(pessoa.get('João')) #Vai retornar NONE
print(pessoa.get('João', {})) #Vai retornar uma chave vazia, só com o parenteses. 


#Método keys -- Retornar apenas as chaves do dicionário 


print(pessoa.keys())

#Método pop()  -- Vai remover um valor/ chave

pessoa.pop('Dalvani', {}) #Removeu 
print(pessoa  ) 

#Método popitem() --- Remove em sequencia, quando terminar de remover ele retrona um KeyError 
pessoa.popitem()

print(pessoa)


pessoa = {
    'nome':{'nome': 'João' , 'idade': 18} ,
    'nome2': {'nome':'Maira', 'idade': 10},
    'nome3': {'nome':'Julia', 'idade' : 18},
    'Dalvani':{'nome': 'Dalvani', 'idade': 37}
} 


#setdefaulf Se o atributo não estiver no dicionário, ele adicona com o valor que eu pedir. Se existir, ele retorna o valor e não altera ele 

pessoa.setdefault('sla', 'Giovanna')
print(pessoa)

#Método update -- Deixa atualiz o dicionário com outro dicionário 

pessoa.update({'nome': {'nome': "jp"}})
print(pessoa)

#Quando colocamos chaves que não existem dentro do dicionário, ele atualiza, adicionando os valores que não tem 
#Values -- Irá retornar todas os valores do dicionario 

print(pessoa.values())


#Método del()  -- Irá excluir o que foi pedido

del pessoa['Dalvani']['idade']  #Irá deletar o valor idade da chave Dalvani 

print(pessoa)

del pessoa['Dalvani']  #Irá deletar toda a chave que foi escrita  

print(pessoa)