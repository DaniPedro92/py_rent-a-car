from auto import printAllAuto, insertAuto, listAuto, searchAuto
from client import insertClient, changeClient, removeClientByNIF, searchClientByNIF, printAllClients, printInfoclient, listClient
from booking import seeListBooking, insertBooking, searchBooking, seeListPastAndFutureBookings, listBooking
from helperfunctions import *
import beaupy

def mainMenu():
    options = [
        "Clientes",
        "Automóveis",
        "Booking",
        "Sair"
    ]
    print("\nMenu:")
    op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
    return str(op)

def clientMenu():
    while True:
        options = [
            "Mostrar Clientes",
            "Adicionar Novo Cliente",
            "Alterar dados de um cliente",
            "Remover um cliente",
            "Pesquisar cliente por NIF e mostrar informações",
            "Voltar"
        ]
        print("\nClientes:")
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1

        if op == 1:
            printAllClients(listClient)
        elif op == 2:
            insertClient(listClient)
        elif op == 3:
            printAllClients(listClient)
            nif_cliente = input("Digite o NIF do cliente que deseja alterar: ")
            cliente_encontrado = False
            for cliente in listClient:
                if cliente['NIF'] == nif_cliente:
                    changeClient(cliente)
                    cliente_encontrado = True
                    break
            if not cliente_encontrado:
                print("Cliente não encontrado.")
            continue  # Volta ao início do loop para exibir o menu novamente
        elif op == 4:
            printAllClients(listClient)
            nif_cliente = int(input("Digite o NIF do cliente que deseja remover: "))
            removeClientByNIF(nif_cliente)
        elif op == 5:
            printAllClients(listClient)
            nif_cliente = int(input("Digite o NIF do cliente que deseja pesquisar: "))
            cliente = searchClientByNIF(nif_cliente)
            if cliente:
                printInfoclient(cliente)
            else:
                print("Cliente não encontrado.")
        elif op == 6:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def autoMenu():
    while True:
        options = [
            "Mostrar Automóveis",
            "Adicionar Novo Automóvel",
            "Pesquisar Automóvel por Matrícula",
            "Voltar"
        ]
        print("\nAutomóveis:")
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
        
        if op == 1:
            printAllAuto(listAuto)
        elif op == 2:
            insertAuto(listAuto)
            writeJSON(listAuto, 'listautomovel.json')
        elif op == 3:
            printAllAuto(listAuto)
            matricula=input("Insira a matricula do automovel que quer pesquisar ex(45-RT-34): ").upper()
            searchAuto(matricula)
        elif op == 4:
            print("A Voltar ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def bookingMenu():
    while True:
        options = [
            "Mostrar Reservas",
            "Adicionar Nova Reserva",
            "Pesquisar Reserva",
            "Sair"
        ]
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
        
        if op == 1:
            seeListPastAndFutureBookings(listBooking)
        elif op == 2:
            newBooking = insertBooking()
            listBooking.append(newBooking)
            writeJSON(listBooking, 'listbooking.json')
        elif op == 3:
            searchBooking()
        elif op == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu():
    while True:
        op = mainMenu()

        if op == '1':
            clientMenu()  
        elif op == '2':
            autoMenu()
        elif op == '3':
            bookingMenu()
        elif op == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
