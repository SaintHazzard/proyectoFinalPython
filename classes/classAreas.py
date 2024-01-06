areas = {}
import json
class areasEntrenamiento:
  def __init__(self,nombre,horario) -> object:
    self.nombre = nombre
    self.horario = horario
    self.ruta = ''
    self.capacidad = 0
    
  def crearJson(self):
        # Ruta del archivo donde guardarás el JSON
      ruta_archivo = f"jsonDataAreas/{self.nombre}{self.horario}.json"
      # Guardar los datos como JSON en un archivo
      with open(ruta_archivo, 'w+') as archivo_json:
          json.dump(self.to_JSON(), archivo_json,indent=4)

      # print(f"Datos guardados en {ruta_archivo}")
      print(f'Area registrada satisfactoriamente')
  def to_JSON(self):
       return{
            "nombre": self.nombre,
            
            "horario" : self.horario,
            "ruta": self.ruta,
            "capacidad": self.capacidad
        }

areas['ApoloMorning'] = areasEntrenamiento('Apolo','Morning shedule')
areas['SputnikMorning'] = areasEntrenamiento('Sputnik','Morning shedule')
areas['ArtemisMorning'] = areasEntrenamiento('Artemis','Morning shedule')
areas['ApoloAfternoon'] = areasEntrenamiento('Apolo','afternoon shedule')
areas['SputnikAfternoon'] = areasEntrenamiento('Sputnik','afternoon shedule')
areas['ArtemisAfternoon'] = areasEntrenamiento('Artemis','afternoon shedule')
for i in areas:
  print(i)
  areas[i].crearJson()

