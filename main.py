from helperfunctions import loadJSON
from auto import printAllAuto, insertAuto, listAuto
from client import seeListClient, addClient
from booking import seeListBooking, addBooking
from menu import mainLoop
"""
listAuto = loadJSON('listautomovel.json')
listBooking = loadJSON('listbooking.json')
listClient = loadJSON('listcliente.json')
 
print("\nCLIENTES:")
print(listClient)
print("\nAUTOMÓVEIS:")
print(listBooking)
print("\nRESERVAS:")
print(listAuto)
"""
 
if __name__ == "__main__":
    mainLoop()
    