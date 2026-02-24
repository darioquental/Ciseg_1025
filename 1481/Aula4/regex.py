import re as reg

# Padrões 
# "ABC"   -----------> procura o padrão ABC no texto
# [A-L]   -----------> procura o padrão A a L no texto
#  *.mp3

#funções

#reg.search()   ------ procura em qualquer parte do texto
#reg.match()    ------ procura no inicio da string
#reg.findall()  ------ devolve todas as ocurrencias na string
#reg.split()    ------ divide a string em partes por padrão


Texto="Eu gosto de Sushi, 25  é dia de jantarada"

resultado = reg.search(r"\d+" ,Texto)

print (resultado)
print (resultado.group())
print (resultado.start())
print (resultado.end())
print (resultado.span())


# r"\d+"  ---- decimal mais um digito