"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

from helperfunctions import writeJSON, readJSON, listAuto, listClient
from auto import printAllAuto
from client import printAllClients
from validatefunctions import validateInt, validateFloat, generateID, findValidID, seeList, validateDate, findItemByID
from datetime import datetime, timedelta
import beaupy

listBooking = readJSON('listbooking.json')

# Função para filtrar listas de reservas (Passadas, a decorrer e futuras)
def filterBookings(listBooking):
    current_date = datetime.now()
    pastBookings = []
    actualBookings = []
    futureBookings = []

    for booking in listBooking:
        booking_start_date = datetime.strptime(booking['data_inicio'], "%d-%m-%Y")
        booking_end_date = datetime.strptime(booking['data_fim'], "%d-%m-%Y")

        if booking_end_date < current_date:
            pastBookings.append(booking)
        elif booking_start_date <= current_date <= booking_end_date:
            actualBookings.append(booking)
        else:
            futureBookings.append(booking)

    pastBookings = sorted(pastBookings, key=lambda x: datetime.strptime(x['data_inicio'], "%d-%m-%Y"))
    actualBookings = sorted(actualBookings, key=lambda x: datetime.strptime(x['data_inicio'], "%d-%m-%Y"))
    futureBookings = sorted(futureBookings, key=lambda x: datetime.strptime(x['data_inicio'], "%d-%m-%Y"))

    return pastBookings, actualBookings, futureBookings

# Função para ver as respectivas listas de reservas
def seeListPastAndFutureBookings(listBooking):
    pastBookings, actualBookings, futureBookings = filterBookings(listBooking)

    print("\nReservas Passadas:")
    seeList(pastBookings, "Reservas")

    print("\nReservas a acontecer:")
    seeList(actualBookings, "Reservas")

    print("\nReservas Futuras:")
    seeList(futureBookings, "Reservas")

# Função para ver listagem de reservas
def seeListBooking(listBooking):
    seeList(listBooking, "Reservas")

# Função para adicionar reversa
def insertBooking():
    print("\nAdicionar nova reserva:")

    # Buscar a lista de cliente e fazer input do ID desejado
    print("\nLista de Clientes disponíveis:\n")
    seeList(listClient, "Clientes") #printa a lista de clientes
    cliente_id = findValidID("ID do Cliente: ", listClient, 'id', "Cliente")
    cliente = findItemByID(cliente_id, listClient)

    # Buscar a lista de automóvel e fazer input do ID desejado
    print("\nLista de Automóveis disponíveis:\n")
    printAllAuto(listAuto)
    automovel_id = findValidID("ID do Automóvel: ", listAuto, 'id', "Automóvel")
    automovel = findItemByID(automovel_id, listAuto)

    # Variaveis para data inicial, numero de dias e a data final
    data_inicio = validateDate("\nData de Início (DD-MM-AAAA): ")
    numeroDias = validateInt("\nQuantos dias quer marcar? ")
    data_fim = data_inicio + timedelta(days=numeroDias)

    # Buscar o preço do automóvel, calcular pelo número de dias e fazer desconto
    precoPorDia = automovel['preco']
    precoReserva = precoPorDia * numeroDias
    if numeroDias <= 4:
        desconto = 1
    elif 5 <= numeroDias <= 8:
        desconto = 0.85
    else:
        desconto = 0.75

    precoDesconto = precoReserva * desconto

    # Dados da nova reserva
    newBooking = {
        'id': generateID(listBooking),
        'data_inicio': data_inicio.strftime("%d-%m-%Y"),
        'data_fim': data_fim.strftime("%d-%m-%Y"),
        'nome_cliente': cliente['nome'],
        'NIF_cliente': cliente['NIF'],
        'marca_auto': automovel['marca'],
        'modelo_auto': automovel['modelo'],
        'matricula_auto': automovel['matricula'],
        'precoPorDia' : precoPorDia,
        'precoReserva': precoReserva,
        'precoDesconto': precoDesconto,
        'numeroDias': numeroDias
    }

    print("\nReserva adicionada com sucesso!")
    return newBooking


# Função para remover uma reserva
def removeBooking(booking_id):
    op = input("Tem certeza que deseja remover esta reserva? (s/n): ").lower()
    if op == "s":
        for booking in listBooking:
            if booking['id'] == booking_id:
                listBooking.remove(booking)
                print(f"Reserva do ID: {booking_id} removida com sucesso!")
                return
        print("Reserva não encontrada com o ID fornecido.")
    elif op == "n":
        print("Remoção cancelada.")
    else:
        print("Resposta inválida!! s para sim, n para não")

# Função para procurar reserva
def searchBooking(listBooking):
    seeListBooking(listBooking)
    userInputID = validateInt("\nID da Reserva que deseja pesquisar: ")
    for i, booking in enumerate(listBooking):
        if booking['id'] == userInputID:
            seeList([booking], "Reserva")
            print("\nOpções:")
            # Menu para escolher dentro da pesquisa se pretende remover ou actualizar
            options = ["Remover Reserva", "Atualizar Reserva", "\033[1;32;1mVoltar\033[m"]
            op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
            if op == 1:
                removeBooking(i)
            elif op == 2:
                updateBooking(userInputID, i, listBooking)  # Adicione listBooking como argumento
            elif op == 3:
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            break
    else:
        print("Reserva não encontrada com o ID fornecido.")

# Função para selecionar o campo a alterar
def selectField(i):
    op = [
        f"Data de Início: {listBooking[i]['data_inicio']}",
        f"Data de Fim: {listBooking[i]['data_fim']}"
    ]
    print("\nCampos disponíveis para atualização:")
    op_index = beaupy.select(op, cursor='->', cursor_style='green', return_index=True)
    return str(op_index + 1)

# Função para modificar campos
def updateBookingFields(op, i):
    while True:
        if op == '1':
            # Actualiza a data_inicio e calcula o numero de dias
            data_inicio = validateDate("Nova Data de Início (DD-MM-AAAA): ")
            new_numero_dias = (datetime.strptime(listBooking[i]['data_fim'], "%d-%m-%Y") - data_inicio).days
            listBooking[i]['data_inicio'] = data_inicio.strftime("%d-%m-%Y")
            listBooking[i]['numeroDias'] = new_numero_dias
            print("\nData de Início da reserva atualizado")
            writeJSON(listBooking, 'listbooking.json')
        elif op == '2':
            # Actualiza a data_final e calcula o numero de dias
            data_fim = validateDate("Nova Data de Fim (DD-MM-AAAA): ")
            listBooking[i]['data_fim'] = data_fim.strftime("%d-%m-%Y")
            new_numero_dias = (data_fim - datetime.strptime(listBooking[i]['data_inicio'], "%d-%m-%Y")).days
            listBooking[i]['numeroDias'] = new_numero_dias
            print("\nData de Fim da reserva atualizado")
            writeJSON(listBooking, 'listbooking.json')

        # Recalcular o precoReservas pelos dias e fazer novamente o desconto
        precoReserva = listBooking[i]['precoPorDia'] * new_numero_dias
        if new_numero_dias <= 4:
            desconto = 1
        elif 5 <= new_numero_dias <= 8:
            desconto = 0.85
        else:
            desconto = 0.75

        precoDesconto = precoReserva * desconto

        listBooking[i]['precoReserva'] = precoReserva
        listBooking[i]['precoDesconto'] = precoDesconto
        
        # Pedir ao user se quer 
        userChoice = input("\nDeseja continuar actualizar (S/N)? ").strip().lower()
        if userChoice == 'n':
            writeJSON(listBooking, 'listbooking.json')
            break
        elif userChoice != 's':
            print("Opção inválida. Por favor, digite 'S' para continuar ou 'N' para sair.")
        else:
            userChoice = selectField(i)

# Função para actualizar a reserva
def updateBooking(userInputID, i, listBooking):
    print("\nAtualizar reserva:")
    seeListBooking(listBooking)
    
    for booking in listBooking:
        if booking['id'] == userInputID:
            seeList([booking], "Reserva")
            print("\nAtualizar Reserva:\n")
            op = selectField(i) 
            updateBookingFields(op, i) 
            break
    else:
        print("Reserva não encontrada com o ID fornecido.")


