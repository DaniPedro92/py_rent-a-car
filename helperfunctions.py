"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

import json
import os.path
 
# operate with json files
 
def loadJSON(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
 
def writeJSON(lista, filename):
    # modos: r (read) a (append) w (write) t (text) b (binary) +
    try:
        with open(filename, 'w') as f:
            json.dump(lista, f, indent=4)
    except:
        print("\nErro: Não foi possível gravar o ficheiro!\n")
    else:
        print(f"\nSucesso: o ficheiro {filename} foi escrito com sucesso!\n")
 
def readJSON(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except:
        #print("\nErro: Não foi possível abrir o ficheiro!\n")
        return []
    else:
        return data
   
# Verificar se o arquivo JSON existe antes de tentar ler
if os.path.exists('listautomovel.json'):
    listAuto = readJSON('listautomovel.json')
else:
    print('Problemas com a sincronização do ficheiro json. Verifique nome e caminho do listautomovel.json')
 
if os.path.exists('listbooking.json'):
    listBooking = readJSON('listbooking.json')
else:
    print('Problemas com a sincronização do ficheiro json. Verifique nome e caminho do listbooking.json')
 
if os.path.exists('listclient.json'):
    listClient = readJSON('listclient.json')
else:
    print('Problemas com a sincronização do ficheiro json. Verifique nome e caminho do listclient.json')