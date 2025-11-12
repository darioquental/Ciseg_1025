listaVazia=[]
listanum=[1,4,5,6,9]
listaString=["Eu adoro pizza","Joao","Rui"]
listaMistas=["ola",2,True]
texto="Eu gosto de python"
# Listas sao indexadas , e aceitam todos os tipos de dados anteriores
# listaString=["Pedro","Joao","Rui"]
#     index  =   0       1      2
#    tamanho =   3 

listanum[0]=9 # subest valor no index escolhido

print(type(listaMistas))
print(listanum)
listanum.insert(0,9) # insere novo elemento na lista e empurra os restantes
print("Usado o metodo insert na posiçao 0",listanum)
listanum.pop(1) # remove a posiçao no index escolhido
print("Usado o metodo pop na posiçao 1",listanum)
listanum.append(11) # adiciona valor no fim da lista
print("Usado o metodo append com valor 11",listanum)
listanum.remove(9) # apaga o primeiro valor encontrado na lista
print("Usado o metodo remove com o valor 9",listanum)
listanum.reverse() # muda a ordem da lista ( ao contrario )
print(listanum)
listanum.reverse()
print(listanum)
listanum.insert(0,9)
print(listanum)

listanum.sort() # ordena a lista 
print("metodo sort para ordenar a lista",listanum)

listasplit=texto.split(" ") # metodo para separa strings ( cria uma lista com as partes separadas)
print(listasplit)

print(listaString[0])
lista2split=listaString[0].split(" ")
print(lista2split)

