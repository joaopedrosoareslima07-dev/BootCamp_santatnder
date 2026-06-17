#Herança em POO - pyhton 
#Herança é a capacidade de uma classe filha herdar ou derivar as caracteristicas, capacidades, comportamentos da classe pai(Base) - Ou seja, é meio que uma herança mesmo.
#Beneficios:
#Representa bem os relacionamentos da vida real | Fornece a reutilização dos códigos, permite adicionar outras caracteristica além da do pai |  É da natureza transitiva, se A classe A herdar as caracteristicas da classe B, todas as subs classe de A herdarão de A. 


#Como declarar uma classe:

class a:
    pass    

class b(a):  # Esse B(a) é assim: estou criando a classe chamada B que vai herdar as caracteristicas de A e ter suas próprias caracteristicas. 
    pass 


#Herança simples: 
#È quando uma classe filha herda apenas de uma clase pai, chamamos de herança simples. 
#Exemplo


class a:
    pass    

class b(a): 
    pass


#herança múltipla:  ---- OBS: Não é todas as linguagens que possuem esse tipo de herança.

#O nome já diz, é que quando uma classe filha herda várias classes pai

#Exemplo:


class a:
    pass    

class b:
    pass
    
class c(a,b): 
    pass