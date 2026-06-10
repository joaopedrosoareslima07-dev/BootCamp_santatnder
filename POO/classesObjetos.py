#Classes são as características e comportamento de um objeto. Porém, não podemos usa-lá diretamente.
#Exemplo 
class cachorro:
    def __init__(self, nome,cor, acordado= True):
        self.nome = nome
        self.cor = cor 
        self.acordado = acordado
        
        
    def latir(self):
        print('AuAuAu')
        
    def dormrindo(self):
        self.acordado = False
        print('ZZZZzzz...')
        
    


#Objetos podemos usar, eles herdarão caracteristicas e comportamentos definidos na classe.
#Chamamos a classe e passamos os valores entre parênteses

cachorro1 = cachorro('Ceneourinha', 'Branco e preto', True)
cachorro2 = cachorro('Balaão', 'Amarelo', False)

cachorro1.latir()


cachorro2.dormrindo()
print(cachorro2.acordado)
