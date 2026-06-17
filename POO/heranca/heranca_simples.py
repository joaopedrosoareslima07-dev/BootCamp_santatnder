class veiculo:
    def __init__(self, cor, placa, ano, qtd_rodas):
            self.cor = cor
            self.placa = placa
            self.ano = ano
            self.qtd_rodas = qtd_rodas
            
    def ligarMotor(self):
        return print('Ligando o motor')
    
    
class moto(veiculo):
        pass
        
    
class carro(veiculo):
    pass    

class caminhao(veiculo):
    def __init__(self, cor, placa, ano, qtd_rodas, num_porta):
         super().__init__(cor, placa, ano, qtd_rodas)

         self.num_porta = num_porta

motinha = moto('Verde', '1234-abc', 2008, 2)      
motinha.ligarMotor()


carro = carro('Branco', '145-cdb', 2026, 4)
carro.ligarMotor()


caminnhao = caminhao('Prata', '1234-abcd', 2025, 12, 2)

print(caminnhao.num_porta)



