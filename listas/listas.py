#Lista é quando uma variável tem uma atribuição de colchetes []

#São usados para armazenar valores, seja strings, int, floats, boolean

#ex:

lista = [1, 'joão', True, 2.5]

print(lista)


#metodos

# append(item): Adiciona um elemento ao final da lista.

#insert(índice, item): Insere um elemento em uma posição específica (índice), empurrando os outros para a direita.

#extend(iterável): Adiciona todos os elementos de outra lista (ou estrutura) ao final da lista atual.

frutas = ['maçã', 'banana']

frutas.append('uva')         # ['maçã', 'banana', 'uva']
frutas.insert(1, 'morango')  # ['maçã', 'morango', 'banana', 'uva']
frutas.extend(['laranja', 'abacaxi']) 
# Resultado: ['maçã', 'morango', 'banana', 'uva', 'laranja', 'abacaxi']


#pop(índice): Remove e retorna o item da posição informada. Se não passar o índice, ele remove o último.

#remove(item): Busca e remove a primeira ocorrência do valor especificado. Se o valor não existir, gera um erro.

#clear(): Limpa a lista completamente, deixando-a vazia [].

numeros = [10, 20, 30, 20, 40]

ultimo = numeros.pop()       # Retorna 40; lista fica: [10, 20, 30, 20]
numeros.remove(20)           # Remove o primeiro 20; lista fica: [10, 30, 20]
numeros.clear()              # Lista fica: []



#sort(): Ordena a lista original em ordem crescente (ou alfabética). Use sort(reverse=True) para ordem decrescente.

#reverse(): Inverte a ordem atual dos elementos na lista (não é uma ordenação, apenas espelha a lista).

letras = ['b', 'c', 'a']
letras.sort()                # ['a', 'b', 'c']

numeros = [1, 5, 3]
numeros.reverse()            # [3, 5, 1]


#count(item): Conta quantas vezes um elemento específico aparece na lista.

#index(item): Retorna o índice (posição) da primeira ocorrência do elemento.

valores = [5, 9, 5, 2, 5]

print(valores.count(5))      # Saída: 3
print(valores.index(9))      # Saída: 1