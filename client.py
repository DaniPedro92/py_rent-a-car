"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

from helperfunctions import *
from validatefunctions import *
from datetime import datetime, timedelta

# Imprimir info de um cliente
def printClient(client):
    print(f"""
    Id: {client['id']} Nome: {client['nome']} NIF: {client['NIF']} DataNascimento: {client['DataNascimento']}
    Telefone: {client['Telefone']} Email: {client['email']}
    """)

# Função para pesquisar um client por NIF
def searchClientByNIF(nif):
    for client in listClient:
        if client['NIF'] == nif:
            return client
    return None

# Listar todos os clientes
def printAllClients(listClient):
    seeList(listClient, "Clientes")

# Função para inserir novo cliente
def insertClient(listClient):
    print("\nInserir dados para registrar o cliente\n")
    nome = input("Nome: ")
    nif = input("NIF: ")
    while any(client['NIF'] == nif for client in listClient):
        print("NIF já existe. Por favor, insira um novo NIF.")
        nif = validateIntLength("NIF: ", 9)

    dataNascimento = validateDate("\nData de Nascimento (DD-MM-AAAA)")

    telefone = validateIntLength("Telefone: ", 9)

    # validação para contém o caracter "@" no meu do imput
    email = input("Email: ")
    while "@" not in email or email.startswith("@") or email.endswith("@"):
        print("Email inválido. Ex: pedromendonça@pymail.pt")
        email = input("Email: ")
    
    # dados para inserir novo cliente
    newClient = {
        'id': generateID(listClient),
        'nome': nome.capitalize(),
        'NIF': nif,
        'DataNascimento': dataNascimento.strftime("%d-%m-%Y"),
        'Telefone': telefone,
        'email': email
    }
    listClient.append(newClient)
    writeJSON(listClient, 'listclient.json')


# Função para alterar os dados do cliente
def changeClient(client):
    print("\nAlterar dados do cliente:")
    alterar_nome = input("Deseja alterar o nome do cliente? (s/n): ")
    if alterar_nome.lower() == "s":
        nome = input("Novo nome: ").capitalize()
        if nome.strip():
            client['nome'] = nome
    alterar_nif = input("Deseja alterar o NIF do cliente? (s/n): ")
    if alterar_nif.lower() == "s":

# Validar novo NIF com 9 dígitos
        nif = input("NIF: ")
        while any(c['NIF'] == nif for c in listClient if c != client):
            print("NIF já existe. Por favor, insira um novo NIF.")
            nif = validateIntLength("Novo NIF: ", 9)
        client['NIF'] = nif
    alterar_data = input("Deseja alterar a Data de Nascimento do cliente? (s/n): ")
    if alterar_data.lower() == "s":
        while True:
            data_nascimento = input("Nova Data de Nascimento (formato dd-mm-aaaa): ")
            birth_date = validateDate(data_nascimento)
            age = (datetime.now() - birth_date) // timedelta(days=365.25)
            if age < 18:
                print("O cliente deve ter mais de 18 anos de idade.")
            else:
                client['DataNascimento'] = data_nascimento
                break
    alterar_telefone = input("Deseja alterar o Telefone do cliente? (s/n): ")
    if alterar_telefone.lower() == "s":
# Validar novo Telefone com 9 dígitos
        telefone = validateIntLength("Novo Telefone: ", 9)
        while any(client['Telefone'] == telefone for client in listClient):
            print("Telefone já existe. Por favor, insira um novo telefone.")
            telefone = validateIntLength("Novo Telefone: ", 9)
        if telefone.strip():
            client['Telefone'] = telefone
    alterar_email = input("Deseja alterar o Email do cliente? (s/n): ")
    if alterar_email.lower() == "s":
        email = input("Novo Email: ")
        if email.strip():
            client['email'] = email
    print("Cliente alterado com sucesso.")
    writeJSON(listClient, 'listclient.json')

# Função para remover um cliente pelo NIF
def removeClientByNIF(nif):
    for client in listClient:
        if client['NIF'] == nif:
            listClient.remove(client)
            print("cliente com NIF", nif, "removido com sucesso.")
            return
    print("NIF", nif, "não encontrado.")

# Função para imprimir as informações do cliente, incluindo as últimas 5 reservas
def printInfoclient(client):
    print("\nInformações do cliente:")
    printClient(client)
    if 'reservas' in client:
        listBooking = client['reservas']
        print("\nÚltimas 5 reservas do cliente:")
        if len(listBooking) >= 5:
            for reserva in listBooking[-5:]:
                print(reserva)
        else:
            print("O cliente não possui 5 reservas.")
    else:
        print("O cliente não possui reservas.")


