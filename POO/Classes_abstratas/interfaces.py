#definem o que uma classe pode fazer 
#Elas não podem ser instânciadas 


#Por padrão o classe não fornece o recurso interface. Usaremos o módulo ABC (abstract base classes)


# Exemplo:

from abc import ABC, abstractmethod

class ControleRemoto(ABC):  
    
    @abstractmethod
    
    def ligar(self):
        pass
    
    @abstractmethod
    
    def desligar(self):
        pass
    
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
        
    def desligar(self):
        print('Desligando TV')



controle = ControleTV()
controle.ligar()

controle.desligar()