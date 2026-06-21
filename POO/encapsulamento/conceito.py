#Conceito de encapsulament!

#É uma forma de proteção aos dados de um objeto!

#Quando não queremos que uma variável seja pública, usamos um encapsulamento.

#Recursos públicos e privados --- Como falamos, o encapsulamento é uma forma de proteção de dados, caso queira que sejam públicos ou proivados. 


#Quando queremos que uma varável de uma classe seja privada usamos uma "_" e quando queremos que seja pública usamos o nome normal 

#O privado é usado apenas dentro da classe 
#exemplo

class Conta:
    def __init__(self, saldo):
        self._saldo = saldo  #Aqui é igual a constante no python, uma boa prática para informar que não devemos mexer nisso, pois seria um atributo privado 
        
    def sacar(self, valor):
        self.valor = valor #Um atributo público.
