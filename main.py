from persona import * 
import os
import json
import pathlib
from visuals import *
clear()

registroAspirantes = {}
rutas={
  
}

for i in registroAspirantes:
  print('-'*50)
  registroAspirantes[i].showData()
  
def from_JSOn():
  acum = {}
  carpeta = 'jsonData/'
  contenidoJsonData = os.listdir(carpeta)

  for item in contenidoJsonData:
      ruta_completa = os.path.join(carpeta, item)
      with open(ruta_completa, 'r') as file:
        datos = json.loads(file.read())
        documento = datos.get('documento')      
        acum[documento] = datos
  return acum
 

registroAspirantes = from_JSOn()

clear()
print((registroAspirantes))