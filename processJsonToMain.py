import os
import json
from classes.classCamper import *

def from_JSOn(carpeta):
  """Lee todos los archivos JSON en la carpeta jsonData/ y los guarda en una variable temporal

  Returns:
      __dict: devuelve un diccionario temporal que se utiliza para convertir cada elemento de este en un objeto
  """
  temporalJson = {}
  contenidoJsonData = os.listdir(carpeta)
  for item in contenidoJsonData:
      ruta_completa = os.path.join(carpeta, item)
      with open(ruta_completa, 'r') as file:
        datos = json.load(file)
        firstKey = datos.get(next(iter(datos))) 
        # print(documento)
        # input('Esperar')
        temporalJson[firstKey] = datos
  return temporalJson



 
def procesarJsonToCamper(CLASE,registroAspirantes,temporalDatosJson):
  """Convierte el dict recibido como @temporalDatosJson en objetos para ser guardados en el
     diccionario del hilo main

  Args:
      registroAspirantes (_dict_): es el diccionario @registroAspirantes del hilo main, donde guardo todos los objetos.
      temporalDatosJson (_dict_): es el return de la funcion @from_JSOn() que se encarga
                                  de leer los archivos con estructura selfnombre.JSON
  """
  
  for dictOb in temporalDatosJson:
    firstKey = next(iter(temporalDatosJson[dictOb]))
    registroAspirantes[dictOb] =  CLASE.from_dict(temporalDatosJson[dictOb])




if __name__=="__name__":
  print('hola')
  pass