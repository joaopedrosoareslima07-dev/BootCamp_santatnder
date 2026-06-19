class Guerreiro:
    def __init__(self, armadura, forca, **sobra):
        self.armadura = armadura
        self.forca = forca
        super().__init__(**sobra)
        
        
class Mago:
    def __init__(self, magia, elemento, **sobra):
        self.magia = magia 
        self.elemento = elemento
       
        
class Paladino(Guerreiro, Mago):
        def __init__(self, armadura, forca,magia, elemento, escudo, **sobra):
             super().__init__(armadura= armadura, forca= forca,magia= magia, elemento = elemento)
             
             
             self.escudo = escudo
    
        
        
personagem = Paladino('Ouro', 99, 100, 'Vento', 100)


print(personagem.__dict__)