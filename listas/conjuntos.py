#É uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados dentro de um iterável.

#exemplo

print(set([1,1,1,2,3,4,5,5]))  #Observamos que ele removeu os números duplicados 


print(set('Abacaxi'))

#Para conseguirmos acesssar os índices do set, teremos que transformar o set em uma lista 


numeros = set([1,1,1,1,2,3,4,5,5])
print(numeros)

numeros = list(numeros)  #Transformamos em lista 

print(numeros[0])


#Métodos do set 
conjuntoA = set([1,2])
conjuntoB = set([3,4])

#union  -- União, como o nome diz, vamos unir eles.
#ex:
print(conjuntoA.union(conjuntoB))


#Intersecção -- intersection 

conjuntoA = set([1,2,2,4])
conjuntoB = set([3,4,1])

print(conjuntoA.intersection(conjuntoB))    #Irá retornar apenas os valores que tem no conjunto A e no conjunto B


#Diferenca  --- Diference  -- Tudo aquilo que está em conjunto mas não está no outro 

conjuntoA = set([1,2,2,4])
conjuntoB = set([3,4,1])

print(conjuntoA.difference(conjuntoB))   #Vai retornar tudo aquilo que possui no conjunto A mas não tem no B
print(conjuntoB.difference(conjuntoA))   #Vai retornar tudo aquilo que possui no conjunto B mas não possui no A



#Diferenca  --- symetric_diference  -- Tudo aquilo que não está em intersecção 

conjuntoA = set([1,2,2,4,5,8,3])
conjuntoB = set([3,4,1,3,5,2])

print(conjuntoA.symmetric_difference(conjuntoB))



#issubset  -- Se é um subconjunto, então todos os elementos de A vai esta em b

print(conjuntoA.issubset(conjuntoB))
print(conjuntoB.issubset(conjuntoA))


#issuperset é o contrário -- todos os elementos de b vão está em A?

print(conjuntoA.issuperset(conjuntoB))
print(conjuntoB.issuperset(conjuntoA))


#isdisjoint

#O isdisjoint() sempre retorna um valor booleano (True ou False):

#Retorna True: Se os conjuntos não possuem nenhum elemento em comum (são disjuntos).

#Retorna False: Se existir pelo menos um elemento igual entre eles.

veganos = {'alface', 'tomate', 'batata'}
carnivoros = {'picanha', 'frango', 'peixe'}

# Eles não têm nada em comum?
print(veganos.isdisjoint(carnivoros))  
# Saída: True (Sim, são totalmente disjuntos!)



#add -- Irá adicionar um elemento, caso não existir 

conjuntoA = set([1,2,2,4,5,8,3])
conjuntoB = set([3,4,1,3,5,2])

conjuntoA.add(100)

print(conjuntoA)


#Clear -- Irá limpar seu set 

conjuntoA = set([1,2,2,4,5,8,3])
conjuntoB = set([3,4,1,3,5,2])

#conjuntoA.clear()
print(conjuntoA)


#O copy irá copiar

#Discard --- Irá descartar um valor 

conjuntoA.discard(2)
print(conjuntoA)


#Método pop
#conjunto.pop(): Remove e retorna um elemento aleatório do conjunto.

numeros = {10, 20, 30, 40}

# Remove alguém que o Python escolher internamente
item_removido = numeros.pop()
print(item_removido)  # Pode ser 10, 20, 30 ou 40
print(numeros)        # O conjunto agora tem 3 elementos


#Remove --  É igual o metodo pop, porem, passamos o valor que queremoa remover 
remove = numeros.remove(20)

print(numeros)

