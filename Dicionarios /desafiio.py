# Lista para armazenar os produtos e preços
carrinho = []
precos = []
quntidade = []
totalProduto = 0
totalCompra = 0


# Loop para adicionar itens ao carrinho
for _ in range(3):
  produtos = input('Informe o nome do produto que você irá comprar ')
  carrinho.append(produtos)
  quantidadeProduto = int(input('Informe quantos produtos você irá pegar ').strip())
  quntidade.append(quantidadeProduto)
  preco = float(input('Informe o preço dos produtos '))
  precos.append(preco)


for i in range(0, len(carrinho)):
  valorQuantidade = quntidade[i]
  valorPreco = precos[i]
  totalProduto = valorQuantidade * valorPreco
  totalCompra += totalProduto
  
  print(f'O produto {carrinho[i]} tem um total de R$ {totalProduto:.2f}')

print()
print(f'A soma dos produtos da lista será {totalCompra}')

