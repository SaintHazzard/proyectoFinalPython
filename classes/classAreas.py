areas = {}
import json
class areasEntrenamiento:
  def __init__(self,nombre) -> object:
    self.nombre = nombre
    # self.ruta = ''
    self.capacidad = {"horarios" : {"morning":{"integrantes":{},"capacidad":0}, "afternoon": {"integrantes":{},"capacidad":0}}}
    
  def crearJson(self):
        # Ruta del archivo donde guardarás el JSON
      ruta_archivo = f"jsonDataAreas/{self.nombre}.json"
      # Guardar los datos como JSON en un archivo
      with open(ruta_archivo, 'w+') as archivo_json:
          json.dump(self.to_JSON(), archivo_json,indent=4)
      # print(f"Datos guardados en {ruta_archivo}")
      print(f'Area registrada satisfactoriamente')
      
  def to_JSON(self):
       return{
            "nombre": self.nombre,
            # "ruta": self.ruta,
            "capacidad": self.capacidad,
        }



