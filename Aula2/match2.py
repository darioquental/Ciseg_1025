66# match é o case em python compara uma variavel para uma igualdade de casos
# só para == / != default

opc=0

while True:

    print("1, 3 , 5 - Bom Dia")
    print("de 6 a 9 - Boa Tarde")
    print("10 , 12 - Boa Noite")
    print("13 - Sair")

    opc=input("Escolha a OPC")

    # print(type(opc)) print para debug

    match opc:
        case "1"| "3" | "5": # if opc==1 or opc==3 or opc==5
            print("Bom Dia")
        case ["6","9"]: # if opc==6 or opc==7 or opc==8 or opc==9
            print("Boa Tarde")
        case "10" | "12": # if opc==10 or opc==12
            print("Boa Noite")
        case "13": # if opc==13
            print("Ate a proxima")
            break # para o while True
        case _: # valores default
            print("Opçao errada")