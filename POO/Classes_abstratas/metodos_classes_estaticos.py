#Métodos de classe e métodos estáticos 

#1. Métodos de Classe (@classmethod)
#O método de classe recebe a própria classe como o primeiro argumento implícito, geralmente chamado de cls (em vez de self). Isso significa que ele tem acesso aos atributos e outros métodos da classe, mas não aos dados de um objeto específico.

#Para que serve: É muito usado como um construtor alternativo (fábricas de objetos) ou para modificar o estado da classe que vai refletir em todas as instâncias.

#exemplo

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
        
    def __str__(self):
        return f'{self.nome} - {self.idade}'
        
        
    @classmethod  
    
    def calcular_idade(cls,nome, ano_atual, ano_nascimento):  # O CLS seria meio que um SELF, porém do método de classe.
        idade = ano_atual - ano_nascimento
        
        return  cls(nome, idade )
    
    
    @staticmethod
    
    def maior_ou_nao(idade):
        if idade >= 18:
         print('Acesso permitido')
            
        else:
         print('Acesso negado')
    
    def mostar_obejto(*obj):
        for x in obj:
            print(x)
            
    
    
    
pessoa = Pessoa('João', 18)  #Criando o objeto da forma normal.

pessoas2 = Pessoa.calcular_idade('Pedro', 2026,2010)  #Usando o método de classe.

Pessoa.mostar_obejto(pessoa, pessoas2)


Pessoa.maior_ou_nao(pessoa.idade)

Pessoa.maior_ou_nao(pessoas2.idade)


#2. Métodos Estáticos (@staticmethod)
#O método estático se comporta exatamente como uma função normal, mas ele vive dentro do escopo da classe apenas por uma questão de organização e lógica. Ele não recebe nem self (objeto) e nem cls (classe). Ele é totalmente isolado.

#Para que serve: Para funções utilitárias. Se a função faz algo relacionado à classe, mas não precisa ler ou alterar nada nela, ela deve ser estática.

