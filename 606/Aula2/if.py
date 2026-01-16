# if estrutura de decisão

# operadores de decisão
# == igualdade 
# != diferente
# > maior que
# >= maior ou igual
# < menor que
# <= menor ou igual
# VALOR1 od VALOR2
#EX. VALOR1 > VALOR2



opc="" # strings

while True:

    print("1 - Bom Dia")
    print("2 - Boa Tarde")
    print("3 - Boa Noite")
    print("4 - Sair")

    opc=input("Escolha a OPC")

    # print(type(opc)) print para debug

    if opc=="1":
        print("Bom dia")
    elif opc=="2":
        print("Boa tarde")
    elif opc=="3":
        print("Boa Noite")
    elif opc=="4":
        print("Ate a proxima")
        break
    else:
        print("Opção errada")