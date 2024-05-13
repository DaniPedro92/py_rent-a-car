from helperfunctions import writeJSON, listAuto, listBooking, listClient
from validadefunctions import generateID, checkInput, seeList, validateFloat, validateInt
import beaupy 


'''#Imprimir as ultimas 5 reservas em caso de menor numero imprime a lista toda
def printReservas(listBooking):
    # Verificar se a lista tem pelo menos 5 reservas
    if len(listBooking) >= 5:
        # Se tiver guarda as últimas 5 reservas
        lastReservas = listBooking[-5:]
        
        # Imprima as últimas 5 reservas
        for reserva in lastReservas:
            print(reserva)
    else:
        print(listBooking)


#listar um carro
def printAuto(auto):
    print(f"""
    Id: {auto['id']} Matrícula: {auto['matricula']} Marca: {auto['marca']} Modelo: {auto['modelo']}
    Cor: {auto['cor']} Portas: {auto['portas']} Preço: {auto['preco']} € Cilindrada: {auto['cilindrada']} Potência: {auto['potencia']}
    """)
'''    

 #listar todos os carros
def printAllAuto(listAuto):
    seeList(listAuto, "Automóveis")

#Inserir 1 carro
def insertAuto(listAuto):
    print("\nInserir dados para registrar o Automóvel\n")        
    while True:
        matricula = input("Matrícula (Exemplo: 31-25-VU, VU-23-45): ").upper()
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
    
    

#Procurar um carro na lista, apresenta os dados do carro juntamente com os 5 ultimos alugueres desse carro (caso seja menor apresenta a lista toda)
#Não obrigamos a inserir obrigatoriamente o campo matricula pois o utilizador pode não saber ou não ter visto na lista o carro pretendido
def searchAuto(matricula):
    while True:
        for auto in listAuto:        
            if auto['matricula'].upper() == matricula:
                seeList([auto], "Detalhes do Carro")
                
                while True:
                    opcao = input("Deseja alterar (A), Eliminar (E) Ver 5 ultimas reservas deste carro (R) ou sair (S)?: ")
                    if opcao.lower() == 'a':
                        # Chame a função para alterar os dados do carro e em seguida atualiza o arquivo JSON
                        changeAuto(auto)
                        writeJSON(listAuto, 'listautomovel.json')
                        break
                    elif opcao.lower() == 'e':
                        # Chame a função para remover o carro aqui
                        removeAuto(auto['matricula'])
                        writeJSON(listAuto, 'listautomovel.json')
                        break
                    # Vai buscar as ultimas 5 reservas desse carro
                    elif opcao.lower() == 'r':
                        lastBookings = [booking for booking in listBooking if booking['matricula_auto'].upper() == matricula][-5:]
                        if lastBookings:
                            print("\nÚltimas 5 reservas associadas a esta matricula:")
                            seeList(lastBookings, "Reservas")
                        else:
                            print("Não há reservas associadas a este carro.")
                        break
                    elif opcao.lower() == 's':
                        print("\nde Volta ao menu...\n")
                        return
                    else:
                        print("Opção inválida. Por favor, escolha novamente.")
                break
        else:
            print("Carro não encontrado.")
            break
            # sai da função após imprimir os dados
    print("Matrícula", matricula, "não encontrada.")


#Função para alterar os dados do carro
def changeAuto(auto):
    print("\nAlterar dados do carro:")
    seeList([auto], "Carro")
    op = selectFieldAuto()
    updateAutoFields(op, auto)

# Função para remover um carro
def removeAuto(matricula):
    matricula = matricula.upper()  # Converter a matrícula para maiúsculas
    for carro in listAuto:
        if carro['matricula'].upper() == matricula:
            listAuto.remove(carro)
            print("Carro com matrícula", matricula, "removido com sucesso.")
            return
    print("Matrícula", matricula, "não encontrada.")

def selectFieldAuto():
    print("Campos disponíveis para actualização:")
    op = ["Marca", "Modelo", "Cor", "Portas", "Preço", "Cilindrada", "Potência"]
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
    else:
        print("Opção inválida.")
    print("Carro alterado com sucesso.")