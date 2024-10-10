#PROGRAMA PARA RESERVA DE QUARTOS HOTEL

import os

# Inicializa as listas e variáveis
registro = []
reservas_pendentes = []

# 2 Suítes Individuais, 2 Suítes Duplas, 2 Quartos Familiares por andar
quartos = {
    1: {'Suíte Individual': [101, 102], 'Suíte Dupla': [103, 104], 'Quarto Familiar': [105, 106]},
    2: {'Suíte Individual': [201, 202], 'Suíte Dupla': [203, 204], 'Quarto Familiar': [205, 206]},
    3: {'Suíte Individual': [301, 302], 'Suíte Dupla': [303, 304], 'Quarto Familiar': [305, 306]}
}

# Dicionário para armazenar a disponibilidade dos quartos
disponibilidade = {
    101: True, 102: True, 103: True, 104: True, 105: True, 106: True,
    201: True, 202: True, 203: True, 204: True, 205: True, 206: True,
    301: True, 302: True, 303: True, 304: True, 305: True, 306: True
}

# Preços dos quartos
p_individual = 180
p_suite_dupla = 300
p_familiar = 500

# Início do programa
while True: 
    os.system("cls")
    print("*" * 20)
    print("*** ESTRELA DO MAR HOTEL ***")
    print("*" * 20)
    print("--- MENU DE RESERVA ---")
    print("Op 1 - Suíte Individual")
    print("Op 2 - Suíte Dupla")
    print("Op 3 - Quarto Familiar")
    print("Op 4 - Preço")
    print("Op 5 - Finalizar Reserva")
    print("Op 6 - Sair do Sistema")

    try:
        opcaoCliente = int(input("Informe a sua opção: "))

    except ValueError:
        print("Erro! A opção deve ser um número!")
        os.system("pause")
        continue

    if opcaoCliente < 1 or opcaoCliente > 6:
        print("Erro! Opção inválida!")
        os.system("pause")
        continue

    if opcaoCliente in [1, 2, 3]:
        os.system('cls')
        
        tipo_quarto = ''
        preco_quarto = 0
        quartos_disponiveis = []

        if opcaoCliente == 1:
            tipo_quarto = 'Suíte Individual'
            preco_quarto = p_individual

        elif opcaoCliente == 2:
            tipo_quarto = 'Suíte Dupla'
            preco_quarto = p_suite_dupla
            
        elif opcaoCliente == 3:
            tipo_quarto = 'Quarto Familiar'
            preco_quarto = p_familiar

        # Coleta os quartos disponíveis do tipo selecionado
        for andar in quartos:
            quartos_disponiveis.extend([q for q in quartos[andar][tipo_quarto] if disponibilidade[q]])

        if not quartos_disponiveis:
            print(f"Desculpe, não há {tipo_quarto.lower()}s disponíveis.")
            os.system('pause')
            continue

        print(f"*** RESERVA {tipo_quarto.upper()} ***")
        print(f"O valor da diária é R$ {preco_quarto:.2f}.")
        
        try:
            dias = int(input("Quantos dias você ficará hospedado? "))
            quantidade = int(input(f"Quantos {tipo_quarto.lower()} você gostaria de reservar? "))
            if quantidade > len(quartos_disponiveis):
                print(f"Desculpe, só temos {len(quartos_disponiveis)} {tipo_quarto.lower()}s disponíveis.")
                os.system('pause')
                continue
            adicionar = int(input("Gostaria de adicionar a reserva? 1 (SIM) 2 (NÃO): "))
        except ValueError:
            print("Erro! Você deve inserir um número inteiro.")
            os.system('pause')
            continue
        if dias < 1:
                print("Erro! Você deve inserir um número inteiro!")
                os.system("pause")
                continue
        if adicionar == 1:
            for i in range(quantidade):
                quarto = quartos_disponiveis[i]
                reservas_pendentes.append((tipo_quarto, quarto, dias, preco_quarto * dias))
                disponibilidade[quarto] = False
            print(f"Reserva adicionada com sucesso.")
        else:
            print("Reserva não adicionada.")
        os.system('pause')

    elif opcaoCliente == 4:
        os.system('cls')
        print("*" * 20)
        print("*** TABELA DE PREÇOS ***")
        print("*" * 20)
        print(f"Suíte Individual: R$ {p_individual:.2f} (1 cama de solteiro)")
        print(f"Suíte Dupla: R$ {p_suite_dupla:.2f} (1 cama de casal)")
        print(f"Quarto Familiar: R$ {p_familiar:.2f} (6 camas de solteiro)")
        os.system('pause')

    elif opcaoCliente == 5:
        os.system('cls')
        if not reservas_pendentes:
            print("Nenhuma reserva foi feita ainda.")
        else:
            valor_total = 0
            print("*** RESERVAS PENDENTES ***")
            for tipo_quarto, quarto, dias, valor in reservas_pendentes:
                print(f"{tipo_quarto} nº {quarto} por {dias} dias. Valor: R$ {valor:.2f}")
                valor_total += valor
            
            print(f"\nTotal a pagar: R$ {valor_total:.2f}")
            try:
                confirmar = int(input("Gostaria de confirmar todas as reservas? 1 (SIM) 2 (NÃO): "))
            except ValueError:
                print("Erro! Você deve inserir um número inteiro.")
                os.system('pause')
                continue

            if confirmar == 1:
                for reserva in reservas_pendentes:
                    registro.append(f"Reserva confirmada no {reserva[0]} nº {reserva[1]} por {reserva[2]} dias. Valor: R$ {reserva[3]:.2f}")
                reservas_pendentes.clear()
                print("Reservas confirmadas com sucesso!")
            else:
                print("Reservas não confirmadas.")
        os.system('pause')

    else:
        os.system('cls')
        print("Saindo do sistema!")
        break
