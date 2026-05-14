#IF -- seria um SE. Se tal coisa acontecer, farei isso
#exemplo:
idade = 18
if idade >= 18:
    print("Maior de idade. ")
    
    
    
#Caso a gente queria 2 validações, usamos o elif .  
#exemplo:
idade = 15
if idade >= 18:
    print('maior de idade ')
    
elif idade <= 15:
    print('Idade entre 15 e 18 anos ')
    

#ELSE -- Seria a ultima validação do cóidigo, caso nenhuma validação em cima dê certo, ele irá cair no else. Ele seria um SENAO
#exemplo: 

idade = 14
if idade >= 18:
    print('maior de idade ')
    
elif idade < 18 and idade >= 15:
    print('Idade entre 15 e 18 anos ')
    
else:
    print('Criança')


