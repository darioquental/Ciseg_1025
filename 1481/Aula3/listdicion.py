listadicionario=[{ "nome":"Joao", "Tele": [965555,989999] },{ "nome":"Pedro", "Tele":[966666,95000]}]

print(listadicionario[2])
for i in range (len(listadicionario)-1):
    for chaves, valor in listadicionario[i].items():
        print (chaves, "  ", valor)


non="Paula"  
ida=24      

listadicionario.append({ "nome":non, "idade": ida })

for i in range (len(listadicionario)):
    for chaves, valor in listadicionario[i].items():
        print (chaves, "  ", valor)


print(listadicionario)
print(listadicionario.items())
print(listadicionario[1]["idade"])