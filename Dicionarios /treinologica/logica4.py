

nome = input('Informe a letra de vc deseja ')
nome = nome.lower().replace(" ", "")  #Aqui estamos deixando o texto de forma padrão, deixando a frase toda minuscula e retirando os espaços 
caracteres = {}   #Criamos um dicionário vazio 

for letra in nome:   #Criamos um loop, que vai passar por toda a palavra, vendo se será repetida 
    if letra in caracteres:    #Criamos uma condição, que para caso a letra já esteja no dicionário, irá adicionar mais um. 
        caracteres[letra] = caracteres[letra] + 1
        
    else: 
        caracteres[letra] = 1 #Caso não estiver, será somente uma letra 

print(caracteres)