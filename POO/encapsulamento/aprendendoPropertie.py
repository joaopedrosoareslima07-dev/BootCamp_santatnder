class CadastroProdutos:
    def __init__(self, nome_produto,preco, quantidade):
        self.nome_produto = nome_produto
        self.preco = preco
        self.quantidade = quantidade
        
    @property 
    def nome_produto(self):
        return self._nome_produto
    
    @nome_produto.setter
    def nome_produto(self, novo_nome ):
      # A validação é feita em cima do 'novo_nome' que acabou de chegar
        if not novo_nome.strip():
            print('O nome não pode ser vazio!')
        else:
            # Se estiver tudo certo, grava na variável interna com SUB-LINHADO
            self._nome_produto = novo_nome
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_valor):
        if novo_valor < 0:
            print('Valor inválido! Insira um valor válido.')
            
            
        else:
            print('Transação concluída. ')
            self._preco = novo_valor
            print (f" Seu novo saldo {self._preco} ")
            
            
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter 
    def quantidade(self, novo_valor_estoque):
        if novo_valor_estoque < 0:
            print('Valor de depósito inválido! ')
            
        else:
            print('Cadastro feito com sucesso')
            
            self._quantidade = novo_valor_estoque
            
            
teste = CadastroProdutos('Iphone 12', 12000, 10)

print(teste.__dict__)

print(teste.nome_produto)

teste.nome_produto = ""
print(teste.nome_produto)

print(teste.preco)

teste.preco = -50

print(teste.preco)

print(teste.quantidade)

teste.quantidade = -70

