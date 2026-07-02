class personagem:
    def __init__(self, nome):
        self.nome = nome 
        
    def atacar(self):
        pass
    
class guerreiro(personagem): 
    def __init__(self, nome):
        super().__init__(nome)
        
    def atacar(self):
        return f'{self.nome} ataca com sua Espada Longa! Causou 15 de dano'
    
class mago(personagem):
    def __init__(self, nome):
        super().__init__(nome)
        
    def  atacar(self):
        return f'{self.nome} lança uma Bola de Fogo! Causou 25 de dano mágico.'
    
    
class Arqueiro(personagem):
    def __init__(self, nome):
        super().__init__(nome)
        
    def  atacar(self):
        return f'{self.nome}  disparou uma flecha certeira! Causou 12 de dano crítico.'
    
    
personagem1 = guerreiro('Pedrinho')
personagem2 = mago('Joãozinho')
personagem3 = Arqueiro('Soarinho')

personagens = [personagem1, personagem2, personagem3]

for check in personagens:
    print(check.atacar())