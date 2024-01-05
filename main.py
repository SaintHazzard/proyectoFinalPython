from persona import * 
import os
import json
import pathlib
from visuals import *


registroAspirantes = {}
rutas={
  
}
# registroAspirantes['0']= Camper('1097910340', 'Oviel 2', 'Mendoza Pineda',3165880900,123123456, 'Cir 36a 104-128 Altos de la Pradera T3-1204', 'Martiza Pineda Celis', 'Aspirante','')


  
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
print(temporalDatosJson)
def procesar_temporal_datos(temporalDatosJson):
    for id in temporalDatosJson:
        print(temporalDatosJson[id])

        documento = temporalDatosJson[id]['documento']
        nombres = temporalDatosJson[id]['nombres']
        apellidos = temporalDatosJson[id]['apellidos']
        movil = temporalDatosJson[id]['movil']
        fijo = temporalDatosJson[id]['fijo'] 
        direccion = temporalDatosJson[id]['direccion']
        acudiente = temporalDatosJson[id]['acuddiente']
        estado = temporalDatosJson[id]['estadon']
        ruta = temporalDatosJson[id]['ruta']
        registroAspirantes[documento] =  Camper(documento, nombres, apellidos, movil, fijo, direccion, acudiente, estado, ruta)


procesar_temporal_datos(temporalDatosJson)
for documento in registroAspirantes:
 registroAspirantes[documento].showData()