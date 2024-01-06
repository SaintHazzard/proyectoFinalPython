import os
import json
from classes.classCamper import *

CARPETAS = ['jsonData/','jsonDataAreas/','jsonDataRutas/']

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


 
def procesarJsonToCamper(CLASE,registroAspirantes,temporalDatosJson : dict):
  """Convierte el dict recibido como @temporalDatosJson en objetos para ser guardados en el
     diccionario del hilo main

  Args:
      registroAspirantes (_dict_): es el diccionario @registroAspirantes del hilo main, donde guardo todos los objetos.
      temporalDatosJson (_dict_): es el return de la funcion @from_JSOn() que se encarga
                                  de leer los archivos con estructura selfnombre.JSON
  """
  
  for dictOb in temporalDatosJson:
    firstKey = next(iter(temporalDatosJson[dictOb]))
    # print(type(temporalDatosJson[dictOb]), '  ', firstKey)
    # print(dictOb)
    registroAspirantes[dictOb]=reInstanciar(CLASE,temporalDatosJson[dictOb])


  
def crearJson(objeto,CARPETA):
  # Ruta del archivo donde guardarás el JSON
  # ruta_archivo = f"{carpeta}/{next(iter(objeto))}.json"
  # Guardar los datos como JSON en un archivo
  with open(CARPETA, 'w+') as archivo_json:
      json.dump(objeto.__dict__, archivo_json,indent=4)
  print(f"Datos guardados en {CARPETA}",end='')
  print(f' {objeto.nombres} registrada satisfactoriamente')

def reInstanciar(CLASE,diccionario):
  # print(CLASE.__dict__)
  # setattr(CLASE, 'documento', 1)
  for clave, valor in diccionario.items():
      # print(valor)
      setattr(CLASE,clave, valor)
      # input('Esperar')
  return CLASE
  
      
      # print(f'clave: {clave}, valor: {valor}')
        
          

class MiClase:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Crear una instancia de la clase
objeto = MiClase(x=10, y=20)

# Mostrar la estructura interna de __dict__


if __name__=="__main__":
  print('hola')
  print(dir(objeto.__dict__))
  pass