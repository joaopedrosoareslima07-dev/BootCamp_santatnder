participantes = int(input('Informe quantos participantes irão participar ').strip())

eventos = {}

for i in range(participantes):
    usuarioTema = input('Informe o seu nome e o tema ').strip()
  
    nome, tema = usuarioTema.split(',')
    
    nome = nome.strip()
    tema = tema.strip()
    
    if tema not in eventos:
        
        eventos[tema] = []
        
    eventos[tema].append(nome)
    
for tema, participantes in eventos.items():
    
    print(f'{tema}: {' , '.join(participantes)} ')
        
        
