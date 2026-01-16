marcas=["BMW","FIAT","TESLA","FORD","FIAT"]
modelos=["M3","PANDA","Model 3","CAPRI","PANDA"]
anos=    [2001,   2002 , 2006   ,  2012 ,  2021 ]
# indice   0    ,  1  ,  2    ,     3  ,   4  
opc=""
valorIntrudProc=""
flagFind=True
flagWhile=True
flagi=0
flagApaga=""
i=0
controleListas=0

#valorIntrudProc e marcas[1]
#    FIAT        e   FIAT 
#   unicode      e    unicode  

while flagWhile:
    i=0
    flagFind=True
    print("1-Remover Marca")
    print("2-Remover Modelo")
    print("3-lista")
    print("4-Sair")
    opc=input("intrud opçao")
    match opc:
        case "1": 
            valorIntrudProc=input("intrud a Marca para remover")
            controleListas=len(marcas)
            while i<controleListas: 
                if valorIntrudProc==marcas[i]: # true or false
                    print("Encontrei a marca na posiçao: ", i , "com o Marca: ", marcas[i],end="")
                    print(" Modelo: ", modelos[i] , " anos: ", anos[i] )
                    flagFind=False
                    flagApaga=input("quer apagar esta Marca , modelo e ano  S/N")
                    if flagApaga=="s" or flagApaga=="S":
                        marcas.pop(i)
                        modelos.pop(i)
                        anos.pop(i)
                        controleWhile-=1
                i+=1
            if flagFind: # mesmo que flagFind == true
                print("Nao existe igualdade")

        case "2":
            valorIntrudProc=input("intrud o Modelo para procurar")
            controleListas=len(modelos)
            while i<controleListas:
                if valorIntrudProc == modelos[i]:
                    print("Encontrei a marca na posiçao: ", i , "com o Marca: ", marcas[i],end="")
                    print(" Modelo: ", modelos[i] , " anos: ", anos[i] )                   
                    flagFind=False
                    flagApaga=input("quer apagar esta Marca , modelo e ano  S/N")
                    if flagApaga=="s" or flagApaga=="S":
                        modelos.pop(i)
                        marcas.pop(i)
                        anos.pop(i)
                        controleListas-=1
                i+=1
            if flagFind: # mesmo que flagFind == true
                print("Nao existe igualdade")

        case "3":
            for i in range(len(marcas)):
                print("Marca: ",marcas[i],"Modelos: ",modelos[i], "Ano: ", anos[i] )
        case "4":
            print("Adeus e obrigado")
            flagWhile=False