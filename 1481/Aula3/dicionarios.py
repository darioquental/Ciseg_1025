# Dicionarios estruturas nao ordenadas ou nao usam index para acesso.
# Acesso a Key , cada key vai ter um ou mais valores.
# {} , acedidos por maping.

dicionario={ "nome":"Joao", "idade": 20 }

print(dicionario)

print("Items : ",dicionario.items())
print("Keys : ",dicionario.keys())
print("Valores : ",dicionario.values())

print("get valor da key nome : ",dicionario.get("nome"))
print("get valor da key idade : ",dicionario.get("idade"))
dicionario.update({"nome":"Luis"})
print (dicionario)
dicionario.update({"nome":"Luis", "idad": 45, "email":"sadas@m.pt" })
print (dicionario)
dicionario["nomeproprio"]=dicionario["nome"]
print (dicionario)
dicionario["nome"]="Pedro"
print (dicionario)
del dicionario[ "idad"]
print (dicionario)

for chave,valor in dicionario.items():
    print(chave , valor)

del dicionario[ "nomeproprio"]

print(end="\n\n\n")
for chave,valor in dicionario.items():
    print(chave , valor)

dicionario["nomeproprio"]=dicionario["nome"]
dicionario.pop("nome")


print(end="\n\n\n")
for chave,valor in dicionario.items():
    print(chave , valor)

dicionario.update({"Tel":92333})

print(end="\n\n\n")
for chave,valor in dicionario.items():
    print(chave , valor)

dicionario.popitem()
print(end="\n\n\n")
for chave,valor in dicionario.items():
    print(chave , valor)

print(dicionario["nomeproprio"])
dicionario["nomeproprio"]="Antonio"

print(end="\n\n\n")
for chave,valor in dicionario.items():
    print(chave , valor)
