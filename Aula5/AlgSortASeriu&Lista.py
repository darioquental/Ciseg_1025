numeros=[2,5,3,1,9]
# index  0,1,2,3,4
opc=""
i=0
controlaOrdenar=True
while True:
    print("1 - Ordenar")
    print("2 - Listar")
    print("3 - Sair")
    opc=input("intrud Opçao")
    match opc:
        case "1":
            controlaOrdenar=True
            while controlaOrdenar:
                controlaOrdenar=False
                i=0
                while i<len(numeros)-1:
                    if numeros[i]>numeros[i+1] :
                        numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
                        controlaOrdenar=True
                    i+=1
        case "2":
            for numero in numeros:
                print("numero : ",numero)
        case "3":
            print(" Bye Bye ")
            break