marcas=[]
modelos=[]
opc=""

while True:
    print("1 - Inserir Marca e Modelo")
    print("2 - Listar")
    print("3 - Sair")
    opc=input("Intrud opçao")
    match opc:
        case "1":
            print("Inserir Marca e depois Modelo")
            print("Marca: ")
            marcas.append(input())
            print("Modelo: ")
            modelos.append(input())
        case "2":
            print("Lista Stand")
            print("Numero Total : ", len(marcas))
            print("Marcas    Modelos")
            for i in range(len(marcas)):
                print(marcas[i] ,"   ",modelos[i])
        case "3":
            print("A sair do Programa")
            break # parar o while True
        case _:
            print("opçao errada")