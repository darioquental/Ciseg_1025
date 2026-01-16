string1="Ola Mundo"
    #    012345678
string2="Ola undo"
    #    012
guardaMenorLista=0
guardaMaiorLista=0
contaComparaCerto=0

print (len(string1)) # 9
print (len(string2)) # 8

if len(string1)>len(string2):
    guardaMenorLista=len(string2)
    guardaMaiorLista=len(string1)

else:
    guardaMenorLista=len(string1)
    guardaMaiorLista=len(string2)

contaComparaCerto=0
for i in range(guardaMenorLista):
    if ord(string1[i])==ord(string2[i]):
        contaComparaCerto+=1
if contaComparaCerto == guardaMaiorLista:
    print ("Strings iguais")
else:
    print("String diferente")