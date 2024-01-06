areas = {}
import json
class areasEntrenamiento:
  def __init__(self,nombre) -> object:
    self.nombre = nombre
    # self.ruta = ''
    self.capacidad = {"horarios" : {"Morning":{"integrantes":{},"capacidad":0}, "Afternoon": {"integrantes":{},"capacidad":0}}}
  def __init__(self,nombre,capacidad) -> object:
    self.nombre = nombre
    # self.ruta = ''
    self.capacidad = {"horarios" : {"Morning":{"integrantes":{},"capacidad":0}, "Afternoon": {"integrantes":{},"capacidad":0}}}
  def printInfoArea(self):
    print("Nombre del area de entrenamiento:", self.nombre)
    print('Horarios')
    capacidad = self.capacidad['horarios']
    clavesHorarios= list(capacidad.keys())
    for i,hora in enumerate(capacidad):
        print(f"\t{hora}: \n\t\tIntegrandes: {capacidad[hora]['integrantes']}")
    
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
       
  # clc es como decir Camper(relleno), es decir instancia la clase con el argumento @data que se le suministra
  @classmethod
  def from_dict(cls, data : dict):
      """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
         para ser almacenado en el diccionario del hilo main

      Args:
          data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

      Returns:
          _Camper_: una instancia de la clase @Camper rellenada
      """
      
      return cls(
            data[next(iter(data))],
            data["capacidad"]
        )



