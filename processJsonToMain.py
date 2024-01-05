import os
import json
from persona import  *

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



def procesarJsonToCamper(registroAspirantes,temporalDatosJson):
    for id in temporalDatosJson:
        documento = temporalDatosJson[id]['documento']
        nombres = temporalDatosJson[id]['nombres']
        apellidos = temporalDatosJson[id]['apellidos']
        movil = temporalDatosJson[id]['telefono']['movil']
        fijo = temporalDatosJson[id]['telefono']['fijo']
        direccion = temporalDatosJson[id]['direccion']
        acudiente = temporalDatosJson[id]['acudiente']
        estado = temporalDatosJson[id]['estado']
        ruta = temporalDatosJson[id]['ruta']
        registroAspirantes[documento] =  Camper(documento, nombres, apellidos, movil, fijo, direccion, acudiente, estado, ruta)





if __name__=="__name__":
  print('hola')
  pass