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
                    'Agência' : agencia,
                    'Numero conta ': numero_conta,
                    'Usuário': verficacao
                }
                

        print('Pessoa não cadastrada ')
        return None
    
def soma(saldo, valor_deposito,extrato,/):
    saldo += valor_deposito
    print('Valor depositado com sucesso! ')
    print(f'Valor atual {saldo:.2f}')
    extrato.append(f' Depósito R$: {valor_deposito}')
    return saldo, extrato
    
def saque(*,saldo, valor_saque, extrato, limite_saque = 500, totalsaque = 0, maximoSaque = 3):
    excedeu_limite_diario = totalsaque >= maximoSaque
    excedeu_limite = valor_saque > limite_saque
    if excedeu_limite_diario:
        print('Limite de saque diário atingido ')
        return saldo, extrato, totalsaque
    elif  excedeu_limite:
        print('Valor do saque maior que o limite permitido ')
        return saldo, extrato, totalsaque
    elif valor_saque < saldo and valor_saque > 0:
        saldo -= valor_saque
        print('Valor sacado com sucesso! ')
        print(f'Valor atual {saldo:.2f}')
        totalsaque += 1
        extrato.append(f' Saque R$: {valor_saque}')
        return saldo, extrato, totalsaque
    
    
def verSaldo(*,saldo):
    print(f'Você tem um saldo de R$: {saldo}')
    
    
def verExtrato(extrato):
    if not extrato:
        print('Não foram realizadas movimentações no banco!')
        
    else:
        for movi in extrato:
            print(movi)
        
extrato = []
saldo = 1000
totalSaque = 0

while True:
        print('''--------------------------------------
                       Bem-Vindo ao banco
                       Escolha sua operação!
                       [01] Criar usuário
                       [02] Criar conta 
                       [03] Depositar 
                       [04] Sacar
                       [05] Ver Saldo 
                       [06] Ver extrato
                       [07] Sair 
                  --------------------------------------
''')
        opcao = int(input('Escolha sua opção: '))

        match opcao:
            case 1:
                criar_usuario(usuarios)

            case 2:    
                numeroConta = len(contas) + 1
                nova_conta = criar_contas(agencia= '0001', numero_conta= numeroConta, usuarios= usuarios)
                
                if nova_conta :
                    contas.append(nova_conta)
                    
            case 3:
                valorDep = float(input('Informe o valor que você deseja depositar '))
                saldo, extrato = soma(saldo, valorDep, extrato)
                
            case 4:
                valorSaque = float(input('Informe o valor que você deseja sacar!: '))
                
                saldo,extrato, totalSaque = saque(saldo= saldo, valor_saque=valorSaque, extrato=extrato, totalsaque= totalSaque)
                
            case 5:
                verSaldo(saldo= saldo)
                
            case 6:
                
                verExtrato(extrato)
                
            case 7:
                print('Saindo...')
                break
            
            case _:
                print('Opção inválida!')
                
            
    
    
    
    