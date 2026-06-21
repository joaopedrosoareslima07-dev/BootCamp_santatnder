#As properties permitem que você transforme um método em algo que pode ser acessado como se fosse um atributo comum, mas com o poder de executar uma lógica (como validação) por trás dos panos.    
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # O sublinhado (_) indica que o atributo é "privado" (protegido)
        self._saldo = saldo_inicial 

    # 1. O GETTER: Permite ler o saldo como se fosse um atributo comum
    @property
    def saldo(self):
        print("Buscando o saldo de forma segura...")
        return self._saldo

    # 2. O SETTER: Executa uma validação antes de alterar o valor
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Erro! O saldo não pode ser negativo.")
        else:
            print("0008000---  Saldo atualizado com sucesso!")
            self._saldo = novo_saldo
            
            
pessoa = ContaBancaria('João Pedro', 7000)

print(pessoa.saldo)

print(pessoa.titular)


pessoa.saldo = 100000

print(pessoa.saldo)
