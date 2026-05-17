print('Olá, seja bem-vindo ao banco!')

extrato = []
qtd_saque = 3
saldo = 1000
while True:
    print("""Informe a operação que você deseja realizar. 
      
      [01] Depositar 
      [02] Sacar
      [03] Ver extrato
      [04] Sair """)

    escolha = int(input("Digite a opção: "))
    match escolha:
        case 1:
            valor_dep = int(input("Informe o valor que você deseja depositar: "))
            
            if valor_dep < 0:
                print("Não foi possivel realizar a operação. ")
                
            else:
                print("Depósto concluído com sucesso!")
                saldo += valor_dep
                extrato.append(f" + {valor_dep:.2f}")
                
        case 2: 
          
                
                valor_saque  = int(input("Informe o valor que você deseja sacar: "))
                if valor_saque > 500:
                    print("Não foi possivel realizae a operação, valor acima do limite! ")
                    
                else:
                    
                    print("Valor sacado com sucesso!")
                    saldo -= valor_saque
                    extrato.append(f" - {valor_saque:.2f}")
                
                qtd_saque -= 1
                
                if qtd_saque == 0:
                    print("Limite de saque diário atingido! ")
                    
        case 3:
            
            print("Seu extrato: ")
            print(extrato)
            print(f"Seu saldo atual. {saldo:.2f}")
                
        case 4: 
            print("Valeu pela preferência!")
            print("Saindo...")
            break