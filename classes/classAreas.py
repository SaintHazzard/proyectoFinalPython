areas = {}
import json
from processJsonToMain import *
class areasEntrenamiento:
  def __init__(self,nombres=None,capacidad=0) -> object:
    self.nombres = nombres
    # self.ruta = ''
    self.capacidad = {"horarios" : 
                          {"6:00 a 10:00":{"integrantes":{},"capacidad":capacidad}, 
                           "10:00 a 14:00": {"integrantes":{},"capacidad":capacidad},
                           "14:00 a 18:00": {"integrantes":{},"capacidad":capacidad},
                           "18:00 a 22:00": {"integrantes":{},"capacidad":capacidad}
                           }}
    
  
  
  
  
  
  def printInfoArea(self):
    print("Nombre del area de entrenamiento:", self.nombres)
    print('Horarios')
    capacidad = self.capacidad['horarios']
    clavesHorarios= list(capacidad.keys())
    for i,hora in enumerate(capacidad):
        print(f"\t{hora}: \n\t\tIntegrandes: {capacidad[hora]['capacidad']}")
  
  def agregarIntegrante(self,integrante,carpeta):
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    print('Indique el horario: ')
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\n")
    if elec in HORARIOS:
      ruta_Archivo = f'{carpeta}{self.nombres}.json'
      # with open(ruta_Archivo, 'r') as archivo_json:
      #   area = json.load(archivo_json)
      strHorario = HORARIOS[elec]
      if self.validarNIntegtrantes(strHorario) and integrante.area is None:
        self.SetearValores(strHorario,integrante)
        with open(ruta_Archivo, "w") as archivo_json:
          json.dump(self.__dict__,archivo_json,indent=4)
  
  def validarNIntegtrantes(self,strHorario):
    if self.capacidad["horarios"][strHorario]["capacidad"] < 33:
      return True
    else: False
    
  def SetearValores(self,strHorario,sujeto):
    integrantes = self.capacidad["horarios"][strHorario]["integrantes"]
    
    if sujeto.documento not in integrantes:
      sujeto.area = self.nombres
      sujeto.horario = strHorario
      crearJson(sujeto,f"{CARPETAS[0]}{sujeto.documento}.json")
      integrantes[sujeto.documento] = sujeto.__dict__
      self.capacidad["horarios"][strHorario]["capacidad"] += 1
    else:
      print('El camper ya esta asignado')





