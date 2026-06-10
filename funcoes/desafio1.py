pacientes = []
urgentes = []
normais = []

def cadastro(*, pacientes, nome, idade, status, pacientesNormais, PacientesUrgentes):
    fichaPaciente = {
        'Nome' : nome,
        'Idade' : idade,
        'Status' : status
    }
    pacientes.append(fichaPaciente)
    
    if fichaPaciente['Status'] == 'Urgente' or fichaPaciente['Idade'] >= 60:
            PacientesUrgentes.append(fichaPaciente  )
            
    else: 
            pacientesNormais.append(fichaPaciente)
            
            
            

cadastro(pacientes= pacientes, nome= 'João', idade= 18, status= 'Normal', pacientesNormais= normais, PacientesUrgentes= urgentes)
cadastro(pacientes= pacientes, nome= 'Pedro', idade= 18, status= 'Urgente', pacientesNormais= normais, PacientesUrgentes= urgentes)
cadastro(pacientes= pacientes, nome= 'Roberto', idade= 86, status= 'Normal', pacientesNormais= normais, PacientesUrgentes= urgentes)

print(f'Lista pacientes {pacientes}')
print(f'Pacientes urgentes {urgentes}')
print(f'Paciente normais {normais}')
    