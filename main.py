from persona import * 
import os
import json
import pathlib
from visuals import *
clear()

registroAspirantes = {}
rutas={
  
}
registroAspirantes['0']= Camper('1097910340', 'Oviel 2', 'Mendoza Pineda',3165880900,123123456, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis', 'Aspirante','')


  
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
 
temporalDatosJson = from_JSOn()

# print(temporalDatosJson)
for ind in temporalDatosJson:
  print(temporalDatosJson[ind])
  registroAspirantes[ind] = Camper(temporalDatosJson[ind]['documento'])
    

