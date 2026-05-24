import random

valor_secreto = random.randint(1,10)

for i in range(1, 4):
    valorDig = int(input('Informe o número que você acha que é '))

    if valorDig > valor_secreto:
        print('O numero digitado está acima do valor secreto ')
        
    elif valorDig < valor_secreto:
        
        print('O número digitado é menor que o valor secreto ')
        
    else:
        
        print('O número digitado é igual ao do sistema! ')