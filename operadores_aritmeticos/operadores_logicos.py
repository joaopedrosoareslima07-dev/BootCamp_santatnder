#São operadores usados para montar uma expressão lógica 

#Operador E ou ---- AND --- Usado quando as duas expressões forem verdadeiras 
#Exemplo:
variavel = 1
variavel2 = 2

if variavel > 0 and variavel2 > 0:
    print("Expressão verdadeira")
    
variavel2 = -2

if variavel > 0 and variavel2 > 0:
    print("Expressão verdadeira")
else:
    print("Expressão falsa")
    
#Operador OU ou -----OR ------ USado quando uma das expressões for verdadeira
variavel2 = -2
variavel = 1

if variavel > 0 or variavel2 > 0:
    print("Expressão verdadeira")
else:
    print("Expressão falsa")
    
    
#Operador de negação  -- NOT ---Sempre vai ser o inverso. Exemplo, 1 > 0 = Verdade (sem o not)-- not 1 > = 0 Falso(usando o not)