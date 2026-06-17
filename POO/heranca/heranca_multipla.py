#É quando queremos pegar caracteristicas de várias classes pai
#ex: 

class pai:
    def __init__(self, nome, **nsei ):
        self.nome = nome
        super().__init__(**nsei)
        
class mae:
    def __init__(self,idade, **nsei):
        super().__init__(**nsei)
        self.idade = idade 
        

class filho(pai, mae):
    def __init__(self, nome, idade, cidade):
        super().__init__(nome = nome, idade= idade) #Aqui ele herdou nome e idade das classes mães 
        
        self.cidade = cidade 
    