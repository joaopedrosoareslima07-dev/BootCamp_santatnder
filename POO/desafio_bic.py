class bicicleta:
    def __init__(self, cor, ano,modelo, valor):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo 
        self.valor = valor
        
    
    def buzinar(self):
        print('Prim Prim')
        
    def parar(self):
        print('Stop ')
        
    def correr(self):
        print('Correndo')
        
        
    
    def __str__(self):
        return f'Modelo: {self.modelo} | Valor: {self.valor} | Ano: {self.ano} | Cor: {self.cor}'
    

bike1 = bicicleta('Preta', 2026, 'GTI', 1950)
        
bike1.buzinar()
bike1.correr()
bike1.parar()

print(bike1)


bike1.ano
bike1.cor