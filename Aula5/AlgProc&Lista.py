marcas=["BMW","FIAT","TESLA","FORD","FIAT"]
modelos=["M3","PANDA","Model 3","CAPRI","PANDA"]
#ano=    [2001,2002    , 2006   ,  2012 ,  2021 ]
# indice   0    ,  1  ,  2    ,     3  ,   4  
opc=""
valorIntrudProc=""
flagFind=True
flagWhile=True

#valorIntrudProc e marcas[1]
#    FIAT        e   FIAT 
#   unicode      e    unicode  

while flagWhile:
    flagFind=True
    print("1-Procura Marca")
    print("2-Procura Modelo")
    print("3-lista")
    print("4-Sair")
    opc=input("intrud opçao")
    match opc:
        case "1": 
            valorIntrudProc=input("intrud a Marca para procura")
            for i in range(len(marcas)):
                if valorIntrudProc==marcas[i]: # true or false
                    print("Encontrei a marca na posiçao: ", i , "com o nome: ", marcas[i])
                    flagFind=False
            if flagFind: # mesmo que flagFind == true
                print("Nao existe igualdade")
            
        case "2":
            valorIntrudProc=input("intrud o Modelo para procura")
            for i in range(len(modelos)):
                if valorIntrudProc == modelos[i]:
                    print("Encontrei a marca na posiçao: ", i , "com o nome: ", modelos[i])
                    flagFind=False
                if flagFind: # mesmo que flagFind == true
                    print("Nao existe igualdade")

        case "3":
            for i in range(len(marcas)):
                print("Marca: ",marcas[i],"Modelos: ",modelos[i])
        case "4":
            print("Adeus e obrigado")
            flagWhile=False