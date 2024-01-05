import os
import json
from classes.classCamper import *

def from_JSOn():
  temporalJson = {}
  carpeta = 'jsonData/'
  contenidoJsonData = os.listdir(carpeta)
  for item in contenidoJsonData:
      ruta_completa = os.path.join(carpeta, item)
      with open(ruta_completa, 'r') as file:
        datos = json.loads(file.read())
        documento = datos.get('documento')      
        temporalJson[documento] = datos
  return temporalJson



def procesarJsonToCamper(registroAspirantes,temporalDatosJson):
    for id in temporalDatosJson:
        documento = temporalDatosJson[id]['documento']
        registroAspirantes[documento] =  Camper.from_dict(temporalDatosJson[id])




if __name__=="__name__":
  print('hola')
  pass