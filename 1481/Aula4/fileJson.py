import os as operating
import json 

objecto={}

filename=R"C:\DEV\Ciseg_0925\Aulas\A4\Data\textoJason.json"

if operating.path.exists(filename):
    with open(filename,'r',encoding='utf-8') as manipfile:
        objecto=json.load(manipfile) # tenta carregar o file json

       
print(objecto)
# no final salvar o novo file

with open(filename,'w',encoding='utf-8') as manipfile:
    json.dump(objecto,manipfile,indent=4,ensure_ascii=False)