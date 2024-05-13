import beaupy
from helperfunctions import *
from validadefunctions import *
import os.path
from datetime import datetime, timedelta

# Verificar se o arquivo JSON existe antes de tentar ler
if os.path.exists('listclient.json'):
    listclient = readJSON('listclient.json')
else:
    listclient = []

# Função para pesquisar um client por NIF
def searchClientByNIF(nif):
    for client in listclient:
        if client['NIF'] == nif:
            return client
    return None


def printClient(client):
    print(f"""
    Id: {client['id']} Nome: {client['nome']} NIF: {client['NIF']} DataNascimento: {client['DataNascimento']}
    Telefone: {client['Telefone']} Email: {client['email']}
    """)

 #listar todos os clientes
def printAllClients(listclient):
    seeList(listclient, "Clientes")

def insertClient(listclient):
    print("\nInserir dados para registrar o cliente\n")
    nome = input("Nome: ")
    nif = validateIntLength("NIF: ", 9)
    while any(client['NIF'] == nif for client in listclient):
        print("NIF já existe. Por favor, insira um novo NIF.")
        nif = validateIntLength("NIF: ", 9)

    dataNascimento = validateDate("\nData de Nascimento (DD-MM-AAAA)")

    telefone = validateIntLength("Telefone: ", 9)

    email = input("Email: ")
    while "@" not in email or email.startswith("@") or email.endswith("@"):
        print("Email inválido. O email deve conter um '@' e não pode estar no início ou no final.")
        email = input("Email: ")
    
    last_client_id = generateID(listclient)
    newClient = {
        'id': last_client_id,
        'nome': nome,
        'NIF': nif,
        'DataNascimento': dataNascimento.strftime("%d-%m-%Y"),
        'Telefone': telefone,
        'email': email
    }
    listclient.append(newClient)
    writeJSON(listclient, 'listclient.json')

# Função para gerar um ID incremental
def generateID(listclient):
    if listclient:
        last_client_id = max(item['id'] for item in listclient)
    else:
        last_client_id = 0
    return last_client_id + 1

# Função para alterar os dados do client
def changeClient(client):
    print("\nAlterar dados do cliente:")
    alterar_nome = input("Deseja alterar o nome do cliente? (s/n): ")
    if alterar_nome.lower() == "s":
        nome = input("Novo nome: ")
        if nome.strip():
            client['nome'] = nome
    alterar_nif = input("Deseja alterar o NIF do cliente? (s/n): ")
    if alterar_nif.lower() == "s":
        # Validar Novo NIF com 9 dígitos
        nif = validateIntLength("Novo NIF: ", 9)
        while any(c['NIF'] == nif for c in listclient if c != client):
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
        # Validar Novo Telefone com 9 dígitos
        telefone = validateIntLength("Novo Telefone: ", 9)
        while any(client['Telefone'] == telefone for client in listclient):
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
    writeJSON(listclient, 'listclient.json')

# Função para remover um client pelo NIF
def removeClientByNIF(nif):
    for client in listclient:
        if client['NIF'] == nif:
            listclient.remove(client)
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


