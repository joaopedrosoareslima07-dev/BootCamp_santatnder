lista = []

caracter = input('Informe o caracter desejado ')

for letra in caracter:
    if letra == '[' or letra == '(':
        lista.append(letra)
        
    elif letra == ')':
        
       if len(lista) == 0 or lista[-1] != '(':
           print('Não pode começar com fechamento')
           break
       else:
           lista.pop()
           
    
    elif letra == ']':
        if len(lista) == 0 or lista[-1] != '[':     
            print('Ordem incorreta ')
            break 
        
        else:
            lista.pop()    
    
    
    
        
        
        
print(lista)