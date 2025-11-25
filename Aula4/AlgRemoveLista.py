marcas=["BMW","FIAT","TESLA","FORD"]
modelos=["M3","PANDA","Model 3","CAPRI"]
# indice   0    ,  1   ,  2      ,  3    
opc=""
removeIndice=0

while True:
    print("1 - Remover")
    print("2 - Listar")
    print("3 - Sair")
    opc=input("intrud opc")
    match opc:
        case "1":
            removeIndice=int(input("intrud indice de carro para remover"))
            marcas.pop(removeIndice)
            modelos.pop(removeIndice)
        case "2":
            print("STAND AUTO")
            for i in range(len(marcas)):
                print("indice : ", i ,"  ",marcas[i],"  ",modelos[i])
        case "3":
            print("sair do programa")
            break
        case _:
            print("opçao errada")