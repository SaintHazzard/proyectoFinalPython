import os
import json
from classes.classCamper import *

CARPETAS = ['jsonData/','jsonDataAreas/','jsonDataRutas/']

def from_JSOn(carpeta : str) -> dict:
  """FUCNION -> READ Lee todos los archivos JSON en la carpeta que se le suministre como argumento y los guarda en una variable temporal
  
  Returns:
      dict : devuelve un diccionario temporal que se utiliza para convertir cada elemento de este en un objeto
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


 
def procesarJsonToCamper(CLASE,registroAspirantes,temporalDatosJson : dict) -> None:
  
  for dictOb in temporalDatosJson:
    firstKey = next(iter(temporalDatosJson[dictOb]))
    # print(type(temporalDatosJson[dictOb]), '  ', firstKey)
    # print(dictOb)
    registroAspirantes[dictOb]=reInstanciar(CLASE,temporalDatosJson[dictOb])

"""Funcion que simula el antiguo From_DICT que reinstanciaba la clase
"""
def reInstanciar(CLASE : classmethod,diccionario:dict) -> object:
  # print(CLASE.__dict__)
  # setattr(CLASE, 'documento', 1)
  instancia = CLASE()
  for clave, valor in diccionario.items():
      # print(valor)
      setattr(instancia,clave, valor)
      # input('Esperar')
  return instancia
  
def crearJson(objeto : object,CARPETA:str) -> None:
  """FUNCION -> ESCRIBE crea los archivos self.JSON

  Args:
      objeto (objeto): Cualquier objeto
      CARPETA (STR): direccion de la carpeta donde se guardaran los JSON
  """
  # Ruta del archivo donde guardarás el JSON
  # ruta_archivo = f"{carpeta}/{next(iter(objeto))}.json"
  # Guardar los datos como JSON en un archivo
  with open(CARPETA, 'w+') as archivo_json:
      json.dump(objeto.__dict__, archivo_json,indent=4)
  print(f"Datos guardados en {CARPETA}",end='')
  print(f' {objeto.nombres} Registro exitoso')


# def to_JSON(diccionario:dict):
#       return json.dumps({
#           "documento": self.documento,
#           "nombres": self.nombres,
#           "apellidos": self.apellidos,
#           "telefono": self.telefonos,
#           "direccion": self.direccion,
#           "acudiente": self.acudiente,
#           "estado": self.estado,
#           "ruta": self.ruta,
#           "notas": self.notas
#       }, indent=4)
      




  """fucnion en desUSO, OBSOLETO remplazado por reInstanciar()
  """
def from_dict(cls, data : dict):
    """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
        para ser almacenado en el diccionario del hilo main

    Args:
        data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

    Returns:
        _Camper_: una instancia de la clase @Camper rellenada
    """
    return cls(
          data['nombres'],
          data['modulos'],
          data["sgdbPrincipal"],
          data['sgdbAlternativo']
      )

  
      
      # print(f'clave: {clave}, valor: {valor}')



