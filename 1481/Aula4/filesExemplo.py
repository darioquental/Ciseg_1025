Texto=""
filename=R"C:\DEV\Ciseg_0925\Aulas\A4\Data\texto.txt"

print(Texto)
with open(filename,'r',encoding='utf-8') as manipfile:
   Texto=manipfile.read()


#menu
#1 inserir Texto append 
print(Texto)
Texto+=" é já amanha"
#2 Listar
#3 Eliminar

#4 Sair || 4 Salvar
with open(filename,'a',encoding='utf-8') as manipfile:
   manipfile.write(Texto)