#Usando o return.

def somatorio (lista):
    return print(sum(lista))

def maior_numero(lista):
    return print(max(lista))


def sucOuAnt (numero):
    sucessor = numero + 1
    antecessor = numero - 1
    
    return  print(antecessor, sucessor)

somatorio([10,50,20,20])
sucOuAnt(25)
maior_numero([50,24,5.40])