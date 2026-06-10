def vericacaoQuartos(*,cadastroquartos, quartoreservado,quarto_que_quer_reservar):
    
    if quarto_que_quer_reservar not in quartoreservado:
        print('Quarto disponível para reserva ')
        quartoreservado.append(quarto_que_quer_reservar)
        print(f'Quartos reservados {quartoreservado}')
    else:
        print('Quarto já reservado, escolha outra opção!')
        print(f'Quartos disponíveis {cadastroquartos}')
    
    return quartoreservado



cadastroQuartos = set(input('Informe os quartos que você deseja cadastrar: ').split(','))
quartoReservado = []

reserva = input('Informe o quarto que você deseja escolher ').split(',')


quartoReservado = vericacaoQuartos(cadastroquartos= cadastroQuartos, quartoreservado= quartoReservado, quarto_que_quer_reservar= reserva)

