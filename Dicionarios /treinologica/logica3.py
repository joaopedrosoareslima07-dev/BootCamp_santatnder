def decoracao():
    print('===================================================')
    
    
def palidromo():
    decoracao()
    palind = input('Informe seu palindromo ')
    palind = palind.lower().replace(" ", "")
      
    palind_invertido = palind[::-1] 
    
    if palind == palind_invertido:
        print('A palavra digitada é um palindromo ')
        
        
    else: 
        print('Não é um palindromo ')
    decoracao()
        
palidromo()