"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

from datetime import datetime
from tabulate import tabulate
#import beaupy
import msvcrt

# Função para validar inteiros
def validateInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")

# Função para validar decimais
def validateFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")

# Função para autoencremento do ID
def generateID(idList):
    if idList:
        lastID = max(item['id'] for item in idList)
    else:
        lastID = 0
    return lastID + 1

# Função para encontrar um ID
def findValidID(msg, entity_list, id_field, entity_type):
    while True:
        id_value = validateInt(msg)
        if any(item[id_field] == id_value for item in entity_list):
            return id_value
        else:
            print(f"ID de {entity_type} inválido. Por favor, insira um {id_field} válido.")

def findItemByID(item_id, item_list):
    for item in item_list:
        if item['id'] == item_id:
            return item
    return None

# Função para não deixar campo vazio
def checkInput(text):
    dado = ""
    while not dado:
        dado = input(text)
    return dado

# Função para usar as teclas para ver lista seguinte ou anterior
def get_key():
    """Função para obter uma tecla pressionada."""
    return msvcrt.getch().decode()

# Função para visualizar as listas com formatação desajada
def seeList(items, list_name):
    if not items:
        print(f"Ainda não temos nenhum(a) {list_name.lower()}.")
        return

    headers = items[0].keys()
    rows = [[item[header] for header in headers] for item in items]
    print(f"\nLista {list_name}:")

    if len(rows) <= 10:
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else:
        start_index = 0
        while True:
            end_index = min(start_index + 10, len(rows))
            current_items = rows[start_index:end_index]
            print(tabulate(current_items, headers=headers, tablefmt="pretty"))

            print("Pressione '\033[1;32mEnter\033[m' para ver 10 seguintes, '\033[1;32mBackspace\033[m' para ver 10 anteriores, ou '\033[1;32mEsc\033[m' para sair.")

            key = get_key()

            if key == "\r":
                if start_index + 10 < len(rows):
                    start_index += 10
                else:
                    print("Você está no final da lista.")
            elif key == "\x08":
                if start_index > 0:
                    start_index -= 10
                else:
                    print("Você está no início da lista.")
            elif key == "\x1b":
                break

# Função para validar datas
def validateDate(msg):
    while True:
        date_str = input(msg)
        try:
            date = datetime.strptime(date_str, "%d-%m-%Y")
            return date
        except ValueError:
            print("Formato de data inválido. Por favor, insira a data no formato DD-MM-AAAA.")

# Função para validar 9 números inteiros: NIF / Telefone
def validateIntLength(msg, length):
    while True:
        value = input(msg).strip()
        if value.isdigit() and len(value) == length:
            return int(value)
        else:
            print(f"Valor inválido. Deve ser um número inteiro com {length} dígitos.")