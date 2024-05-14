"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

import beaupy
from auto import listAuto, insertAuto, searchAuto, printAllAuto, changeAuto,removeAuto,findAutoByMatricula
from client import listClient, insertClient, changeClient, removeClientByNIF, searchClientByNIF, printInfoclient, printAllClients
from booking import listBooking, seeListBooking, insertBooking, searchBooking, seeListPastAndFutureBookings
from helperfunctions import writeJSON
from validatefunctions import checkInput, seeList
from intro import introAnimation, introAnimationOut

# Função menu principal        
def mainMenu():
    options = [
        "Clientes",
        "Automóveis",
        "Booking",
        "Sair"
    ]
    print("\nMenu Principal:\n")
    op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
    return str(op)

# Função menu cliente
def clientMenu():
    while True:
        options = [
            "Mostrar Clientes",
            "Adicionar Novo Cliente",
            "Alterar dados de um cliente",
            "Remover um cliente",
            "Pesquisar cliente por NIF e mostrar informações",
            "\033[1;32;1mVoltar\033[m"
        ]
        print("\nMenu Clientes:")
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
 
        if op == 1:
            printAllClients(listClient)
        elif op == 2:
            insertClient(listClient)
            writeJSON(listClient, 'listclient.json')  
        elif op == 3:
            nif_client = input("Digite o NIF do cliente que deseja alterar: ")
            client_encontrado = False
            for client in listClient:
                if client['NIF'] == nif_client:
                    seeList([client], "Reserva")
                    changeClient(client)
                    client_encontrado = True
                    break
            if not client_encontrado:
                print("cliente não encontrado.")
            continue
        elif op == 4:
            nif_client = input("Digite o NIF do cliente que deseja remover: ")
            removeClientByNIF(nif_client)
        elif op == 5:            
            nif_client = input("Digite o NIF do cliente que deseja pesquisar: ")
            client = searchClientByNIF(nif_client)
            if client:
                printInfoclient(client)
            else:
                print("cliente não encontrado.")
        elif op == 6:
            print("A Voltar ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
 
        voltar_menu = input("\nDeseja voltar ao menu cliente? (s/n): ")
        if voltar_menu.lower() != "s":
            break
 
    writeJSON(listClient, 'listclient.json')

# Função menu automóvel
def autoMenu():
    while True:
        options = [
            "Mostrar frota de Automóveis",
            "Adicionar Automóveis á frota",
            "Alterar dados de um Automóvel",
            "Remover Automóveis da frota",
            "Pesquisar Automóvel por Matrícula",
            "\033[1;32;1mVoltar\033[m"
        ]
        print("\nMenu Automóveis:\n")
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
        
        if op == 1:
            printAllAuto(listAuto)
        elif op == 2:
            insertAuto(listAuto) 
        elif op == 3:
            while True:
                matricula = input("Insira a '\033[1;32;1mMatrícula\033[m' do automóvel que quer alterar (Exemplo: 45-RT-34) ou '\033[1;32mS\033[m' para voltar ao menu anterior: ").upper()
                if matricula == 'S':
                    break
                auto = findAutoByMatricula(matricula)  # Função para encontrar o carro pela matrícula
                if auto is not None:
                    changeAuto(auto)
                    break
        elif op == 4:
            matricula = checkInput("Insira a '\033[1;32;1mMatrícula\033[m' do automóvel que quer remover (Exemplo: 45-RT-34) ou '\033[1;32mS\033[m' para voltar ao menu anterior: ").upper()
            removeAuto(matricula)   
        elif op == 5:
            matricula=checkInput("Insira a '\033[1;32;1mMatrícula\033[m' do automovel que quer pesquisar ex(45-RT-34): ").upper()
            searchAuto(matricula)  
        elif op == 6:
            print("A Voltar ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Função menu booking/reservas
def bookingMenu():
    while True:
        options = [
            "Mostrar Reservas",
            "Adicionar Nova Reserva",
            "Pesquisar Reserva",
            "\033[1;32;1mVoltar\033[m"
        ]
        print("\nBooking:")
        op = beaupy.select(options, cursor='->', cursor_style='green', return_index=True) + 1
       
        if op == 1:
            seeListPastAndFutureBookings(listBooking)
        elif op == 2:
            newBooking = insertBooking()
            listBooking.append(newBooking)
            writeJSON(listBooking, 'listbooking.json')
        elif op == 3:
            searchBooking(listBooking)
        elif op == 4:
            print("A Voltar ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# iniciação do menu e intro
def menu():
    introAnimation()

    while True:
        op = mainMenu()

        if op == '1':
            clientMenu()  
        elif op == '2':
            autoMenu()
        elif op == '3':
            bookingMenu()
        elif op == '4':
            introAnimationOut()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
