class Veiculo:
    def __init__(self, roda, cor, placa, **repasse):
        self.roda = roda
        self.cor = cor 
        self. placa = placa 
        super().__init__(**repasse)
        
class Carro():
    def __init__(self,  marca, ano, **repasse):
        super().__init__(**repasse)
        
        self.marca = marca 
        self.ano = ano 
        

class Eletrico(Veiculo, Carro):  
        def __init__(self, roda, cor, placa,marca, ano, bateria, **repasse):
             super().__init__(roda= roda, cor = cor, placa=placa, marca= marca, ano=ano)
             self.bateria = bateria
             
             
# Criando o objeto
meu_eletrico = Eletrico(
    roda=4, 
    cor="Azul", 
    placa="AAA-123", 
    marca="BYD", 
    ano=2025, 
    bateria="75 kWh"
)

# Printando para checar se o repasse funcionou
print(f"Marca: {meu_eletrico.roda}")
print(f"Placa: {meu_eletrico.cor}")
print(f"Bateria: {meu_eletrico.ano}")
    