#São operadores ultilizados para saber se dois objetos testados ocupam a mesma posição  na memória 
#Exemplo:
#objeto1 IS objeto2

saldo = 1000
limite = 500
print(saldo is limite)  #Não ocupam a mesma região 

print(saldo is not limite)

saldo = 1000
limite = 1000
print(saldo is limite)  #Ocupam a mesma região de memória 

print(saldo is not limite)   #Não ocupam 