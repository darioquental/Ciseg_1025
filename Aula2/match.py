# match é o case em python compara uma variavel para uma igualdade de casos
# só para == / != default


opc=0

while True:

    print("1 - Bom Dia")
    print("2 - Boa Tarde")
    print("3 - Boa Noite")
    print("4 - Sair")

    opc=input("Escolha a OPC")

    # print(type(opc)) print para debug

    match opc:
        case "1": # opc==1
            print("Bom Dia")
        case "2": # opc==2
            print("Boa Tarde")
        case "3": # opc==3
            print("Boa Noite")
        case "4": # opc==4
            print("Ate a proxima")
            break
        case _: # default
            print("Opçao errada")