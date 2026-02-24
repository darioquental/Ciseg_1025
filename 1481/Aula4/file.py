# 1 passo : Abrir o file
# with open()
# 2 passso Modos de açao no file
#- modos de abertura:
# 'r' leitura (read)
# 'w' escrita (write)
# 'a' acrescentar  (write)
# 'b' 'wb' ou'rb' binario
# 'x' criar novo ficheiro
# 3 fechar o ficheiro 
# exemplo ficheiro.close() -> nao nesserio com with open()

filename=R"C:\DEV\Ciseg_0925\Aulas\A4\Data\texto.txt"

with open(filename,'r',encoding='utf-8') as manipfile:
   Texto=manipfile.read()

# no final salvar o novo file

with open(filename,'w',encoding='utf-8') as manipfile:
   manipfile.write(Texto)