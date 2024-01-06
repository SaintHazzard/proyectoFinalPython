areas = {}
import json
class areasEntrenamiento:
  def __init__(self,nombres=None,capacidad=0) -> object:
    self.nombres = nombres
    # self.ruta = ''
    self.capacidad = {"horarios" : {"Morning":{"integrantes":{},"capacidad":0}, "Afternoon": {"integrantes":{},"capacidad":0}}}
  def printInfoArea(self):
    print("Nombre del area de entrenamiento:", self.nombres)
    print('Horarios')
    capacidad = self.capacidad['horarios']
    clavesHorarios= list(capacidad.keys())
    for i,hora in enumerate(capacidad):
        print(f"\t{hora}: \n\t\tIntegrandes: {capacidad[hora]['integrantes']}")
      
  def to_JSON(self):
       return{
            "nombres": self.nombres,
            # "ruta": self.ruta,
            "capacidad": self.capacidad,
        }
       




