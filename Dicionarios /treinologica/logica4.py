

nome = input('Informe a letra de vc deseja ')
nome = nome.lower().replace(" ", "")
caracteres = {}

for letra in nome:
    if letra in caracteres:
        caracteres[letra] = caracteres[letra] + 1
        
    else: 
        caracteres[letra] = 1
        

print(caracteres)