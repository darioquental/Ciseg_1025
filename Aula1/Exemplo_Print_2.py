# input()  le o que escremos no terminal

nome=""
altura=0.0     # tipo float numeros com virgula (.)
num1=0

print("Intrud a seu nome")
nome=input()

print(type(nome))

    # float <---- String     casting    
altura=float(input("intrud a sua altura"))

print(type(altura))

    # Int <---- String     casting   
num1=int(input("intrud a um numero"))

print(type(num1), end="\n\n")

print(f"este é o seu nome : {nome} e a sua altura é  {altura} e a seu numero é  {num1}" )
