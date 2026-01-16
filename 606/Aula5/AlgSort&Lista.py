numeros=[2,5,3,1,9]
opc=""

while True:
    print("1 - Ordenar")
    print("2 - Listar")
    print("3 - Sair")
    opc=input("intrud Opçao")
    match opc:
        case "1":
            numeros.sort()
        case "2":
            for numero in numeros:
                print("numero : ",numero)
        case "3":
            print(" Bye Bye ")
            break