# Variáveis de classes e Variáveis de instância.

#É o atributo que pertence a um objeto específico (à cópia que você criou). Se você altera em um personagem, não muda nos outros.
#Exemplo: O nome do personagem, a vida atual, a força.


#2. Variável de Classe
#É o atributo que pertence à classe como um todo. Ela é compartilhada por todas as instâncias criadas a partir dali. Se você altera o valor na classe, todo mundo vê a mudança.
#Exemplo: O nome do jogo, o limite máximo de poções que qualquer personagem pode carregar.


class FPS:
    vida = 100
    
    def __init__(self, nome, habilidade):
        self.nome = nome 
        self.habilidade = habilidade
        
        
    def __str__(self):
        return f'{self.nome} - {self.vida} - {self.habilidade}'
    
    
def mostrarValores(*x):
        for obj in x:
            print(obj)
            
            
            

teste1 = FPS('Hayato', 'Precisão')
teste2 = FPS('Kelly', 'Correr')


mostrarValores(teste1, teste2)



FPS.vida = 25 #Aqui ambos ficaram com a vida de 25, pois mudamos a variável de classe.

mostrarValores(teste1, teste2)


teste1.vida = 50  # Aqui mudamos apenas o valor da vida do objeto 1. Pois, mudamos apenas a variável de instância do objeto 1.

mostrarValores(teste1, teste2)