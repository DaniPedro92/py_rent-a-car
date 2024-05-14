"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

from helperfunctions import writeJSON, listAuto, listBooking
from validatefunctions import generateID, checkInput, seeList, validateFloat, validateInt
import beaupy 
from datetime import datetime

#listar todos os carros
def printAllAuto(listAuto):
    seeList(listAuto, "Automóveis")

#Inserir 1 carro
def insertAuto(listAuto):
    print("\nInserir dados para adicionar o novo Automóvel:\n")        
    while True:
        matricula = input("Digite a '\033[1;32;1mmatrícula\033[m' (Exemplo: 31-25-VU, VU-23-45) ou '\033[1;32mS\033[m' para voltar ao menu anterior: ").upper()
        if matricula == 'S':
            print("Voltando ao menu anterior...")
            return
        partes = matricula.split('-')
        if len(partes) == 3 and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 2 and partes[0].isalnum() and partes[1].isalnum() and partes[2].isalnum():
            matriculaExiste = False
            for auto in listAuto:
                if auto['matricula'].upper() == matricula:
                    matriculaExiste = True
                    break
            if not matriculaExiste:
                break
            else:
                print("Matrícula já existe. Por favor, insira uma nova matrícula.")
        else:
            print("Por favor, insira uma matrícula válida no formato (Exemplo: 31-25-VU, VU-23-45).")
 
    #Validações para obrigar a nao deixar o campo vazio e definir o tipo de campo
    marca = checkInput("Marca: ")
    modelo = checkInput("Modelo: ")
    cor = checkInput("Cor: ")
    portas = validateInt("Portas: ")
    preco = validateFloat("Preço: ")
    cilindrada = validateFloat("Cilindrada: ")
    potencia = validateInt("Potência: ")
    newCar = {
        'id' : generateID(listAuto),
        'matricula': matricula.upper(),
        'marca': marca,
        'modelo': modelo,
        'cor': cor,
        'portas': portas,
        'preco': preco,
        'cilindrada': cilindrada,
        'potencia': potencia
    }
    #Actualizamos a lista
    listAuto.append(newCar)
    writeJSON(listAuto, 'listautomovel.json')
    
#Procurar um carro na lista, apresenta os dados do carro juntamente com os 5 ultimos alugueres desse carro (caso seja menor apresenta a lista toda)
#Apresenta apenas os alugueres desse carro que foram finalizados até a data da pesquisa.
def searchAuto(matricula):
    auto_encontrado = False
    for auto in listAuto:        
        if auto['matricula'].upper() == matricula:
            auto_encontrado = True
            seeList([auto], "Detalhes do Carro")
            opcao = input("Deseja ver as 5 últimas reservas deste carro '\033[1;32;1m(R)\033[m' ou voltar ao menu automóvel '\033[1;32;1m(S)\033[m'?: ")
            if opcao.lower() == 'r':
                current_date = datetime.now()
                lastBookings = [booking for booking in listBooking if booking['matricula_auto'].upper() == matricula and datetime.strptime(booking['data_fim'], '%d-%m-%Y') <= current_date][-5:]
                if lastBookings:
                    print("\nÚltimas 5 reservas associadas a esta matrícula e com data de término anterior à data atual:")
                    seeList(lastBookings, "Reservas")
                else:
                    print("Não há reservas associadas a este carro.")
            elif opcao.lower() == 's':
                print("\nVoltando ao menu Automóveis...\n")
                return
            else:
                print("Opção inválida. Por favor, escolha novamente.")
            break
    if not auto_encontrado:
        print("Carro não encontrado.")

# Função para encontrar o carro pela matrícula para em seguida fazer alterações dos campos que pretender
def findAutoByMatricula(matricula):
    partes = matricula.split('-')
    if len(partes) == 3 and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 2 and partes[0].isalnum() and partes[1].isalnum() and partes[2].isalnum():
        for auto in listAuto:
            if auto['matricula'].upper() == matricula:
                return auto
        print("Automóvel não encontrado.")
    else:
        print("Por favor, insira uma matrícula válida no formato (Exemplo: 31-25-VU, VU-23-45).")
    return None

#Função para alterar os dados do carro
def changeAuto(auto):
    print("\nAlterar dados do carro:")
    seeList([auto], "Carro")
    while True:
        op = selectFieldAuto()
        if op == '8':
            break
        updateAutoFields(op, auto)

#função para alterar/selecionar o campo que queremos alterar com o beaupy
def selectFieldAuto():
    print("Campos disponíveis para actualização:")
    op = ["Marca", "Modelo", "Cor", "Portas", "Preço", "Cilindrada", "Potência", "\033[1;32;1mVoltar\033[m"]
    selectedOption = beaupy.select(op, cursor='->', cursor_style='green', return_index=True) + 1
    return str(selectedOption)
 
#Recebe os dados validando cada um deles
def updateAutoFields(op, auto):
    if op == '1':
        auto['marca'] = checkInput("Nova marca: ")
    elif op == '2':
        auto['modelo'] = checkInput("Novo modelo: ")
    elif op == '3':
        auto['cor'] = checkInput("Nova cor: ")
    elif op == '4':
        auto['portas'] = validateInt("Novas portas: ")
    elif op == '5':
        auto['preco'] = validateFloat("Novo preço: ")
    elif op == '6':
        auto['cilindrada'] = validateFloat("Nova cilindrada: ")
    elif op == '7':
        auto['potencia'] = validateInt("Nova potência: ")
    elif op == '8':
        return
    else:
        print("Opção inválida.")
    print("Carro alterado com sucesso.")

# Função para remover um carro
def removeAuto(matricula):
    if matricula.upper() == 'S':
        print("Voltou ao menu anterior...")
        return

    matricula = matricula.upper()  # Converter a matrícula para maiúsculas
    for carro in listAuto:
        if carro['matricula'].upper() == matricula:
            listAuto.remove(carro)
            writeJSON(listAuto, 'listautomovel.json')
            print("Carro com matrícula", matricula, "removido com sucesso.")
            return
    print("Matrícula", matricula, "não encontrada.")


