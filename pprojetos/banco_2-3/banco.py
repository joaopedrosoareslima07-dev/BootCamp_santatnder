contas = []
usuarios = []


def criar_usuario(usuarios):
    cpf = input('Informe seu CPF ')
    
    for verificar in usuarios:
        if verificar['Cpf'] == usuarios:
         return print('Usuário ja cadastrada!')
    
    nome = input('Informe seu nome completo: ')
    
    idade = int(input('Informe sua idade'))
    
    if idade < 18 or idade < 0:
        print('Data de nascimento inválida!')
        
    cidade = input('Informe sua cidade: ')
    logradouro = input('Informe seu logradouro ')
    numeroCasa = input('Informe o número da sua casa ')
    bairro = input('Informe o seu bairro ')
    
    endereco = (f'{cidade},{bairro}, {logradouro}, {numeroCasa} ')
    
    dados_usuarios = {
        
        'nome' : nome,
        'Idade' : idade,
        'Endereço' : endereco,
        'Cpf' : cpf
    }
    
    usuarios.append(dados_usuarios)
    print('Cadastro realizado com sucesso! ')
    
    
    def criar_contas(agencia, numero_conta, usuarios):
        pedidoCpf = input('Informe seu CPF: ')
        for verficacao in usuarios:
            if pedidoCpf == verficacao['Cpf']:
                
                
                return  {
                    'Agência' : '0001',
                    'Numero conta ': numero_conta,
                    'Usuário': verficacao
                }
                
        else:
            print('Pessoa não cadastrada ')



    
    
    
    
    
    
    