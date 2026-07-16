#POO - Classe e objeto

#É um paradigma de programação que usa "objetos" para representar dados e comportamentos.

#Classe: É o "molde" ou a planta baixa. --- Será o lugar que terá característica, comportamentos do objeto.

#Objeto: É a instância real criada a partir desse molde. --- Ou seja, será coisas criadas usando o objeto como exemplo. 

# __init__ (Construtor): O método especial que inicializa os atributos do objeto quando ele é criado. -- Será as características iniciais do objeto/classe

#self: Representa a própria instância do objeto que está sendo operada. 

#exemplo: 
class carro:
    def __init__(self, marca, placa, modelo, ano, cor):
        self.marca = marca
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Placa: {self.placa} | Cor: {self.cor} | Ano: {self.ano}' 

    def __str__(self):
        return f'{self.__class__.__name__}:  {' | '.join([f'{chave} : {valor}'  for chave, valor in self.__dict__.items()])}'
    
    
    def mostrar(*most):
        for x in most:
            print(x)
    
carro1 = carro('Celta', '123-abc', 'Atual', 2008, 'Vermelho')





#Formas de impressão.

print(carro1.__dict__)  #imprimir o conteúdo da classe carro1 em um dicionário.

print(carro1)  #Aqui criamos uma função dentro da nossa classe que retorna os valores do objeto.

print(f'Marca: {carro1.marca} | Modelo: {carro1.modelo} | Placa: {carro1.placa} | Ano: {carro1.ano} | Cor: {carro1.cor}') #Aqui a gente cria uma f-string para mostrar todos os parametros do objeto.

print(carro1)

carro.mostrar(carro1)