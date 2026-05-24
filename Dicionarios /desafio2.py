# 1ª  Pedir nome e Tema
#2ª Fazer a validação 
#3ª Dividir os participantes e imprimir 
fotografia = []
danca = []
musica = []
tecnologia = []
esportes = []


for i in range(3):
    nome = input('Informe seu nome, por favor!', ).strip()
    tema = input('Informe o tema ').strip()
    print()
    
    if tema == 'fotografia': 
        fotografia.append([nome, tema])
    
    elif tema == 'danca': 
        danca.append([nome, tema])
    
    elif tema == 'musica': 
        musica.append([nome, tema])
    elif tema == 'tecnoligia': 
        tecnologia.append([nome, tema])
    elif tema == 'esportes': 
        esportes.append([nome, tema])
        
        
print(f'Fotografia {fotografia}')

print(f'Dança {danca}')

print(f'Musica {musica}')

print(f'Tecnologia {tecnologia}')

print(f'Esportes {esportes}')