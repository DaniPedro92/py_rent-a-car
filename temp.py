from helperfunctions import readJSON, writeJSON
 
# functions
def insertAuto():
    print("\nInserir Automóvel\n")
    matricula = input("Matrícula: ")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    cor = input("Cor: ")
    preco = float(input("Preço: "))
    return {'matricula' : matricula, 'modelo' : modelo, 'marca' : marca, 'cor' : cor, 'preco' : preco}
 
def printAuto(auto):
    print(f"""
    Matrícula: {auto['matricula']} Marca: {auto['marca']} Modelo: {auto['modelo']}
    Cor: {auto['cor']} Preço: {auto['preco']} €
    """)
 
def printAllAuto(listAuto):
    print("\nListagem de automóveis\n")
    if listAuto:
        for auto in listAuto:
            printAuto(auto)
    else:
        print("\nAinda não foram adicionados automóveis!\n")
 
 
def search(**kwargs):
    cor = kwargs.get('cor', None) # isolar a chave
    precoMin = kwargs.get('precoMin', None) # isolar a chave
    precoMax = kwargs.get('precoMax', None) # isolar a chave
   
    if listAuto:
        count = 0
        if cor:
            print("\nPesquisa pelo critério cor:")
            for auto in listAuto:
                if auto['cor'].lower() == cor.lower(): # filtro
                    printAuto(auto)
                    count +=1
        if precoMin and precoMax:
            print(f"\nPesquisa pelo critério preço [{precoMin} : {precoMax}]:")
            for auto in listAuto:
                if precoMin <= auto['preco'] <= precoMax: # filtro
                    printAuto(auto)
                    count +=1
        if not count:
            print("\nNão foram encontrados automóveis com o perfil indicado!\n")
    else:
        print("\nAinda não foram adicionados automóveis!\n")  
 
 
def menu(listAuto, filename):
    while True:
        print("1 - Inserir Automóvel")
        print("2 - Listagem Automóveis")
        print("3 - Pesquisa")
        print("4 - Sair")
        op = int(input("Indique a opção desejada: "))
        match op:
            case 1:
                listAuto.append(insertAuto())
                writeJSON(listAuto, filename)
            case 2:
                printAllAuto(listAuto)
            case 3:
                #search(cor = input("Cor: "))
                search(precoMin = float(input("Preço Mínimo: ")), precoMax = float(input("Preço Máximo: ")))
 
            case 4:
                break
            case _:
                print("\nErro. Opção inválida\n")
 
 
# globals
filename = "files/automoveis.json"
listAuto = []
 
# load initial content
listAuto = readJSON(filename)
 
# menu
menu(listAuto, filename)