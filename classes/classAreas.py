areas = {}
import json
from processJsonToMain import *
class areasEntrenamiento:
  def __init__(self,nombres=None,capacidad=0) -> object:
    self.nombres = nombres
    # self.ruta = ''
    self.horarios = {"6:00 a 10:00":{"integrantes":{},"capacidad":capacidad}, 
                           "10:00 a 14:00": {"integrantes":{},"capacidad":capacidad},
                           "14:00 a 18:00": {"integrantes":{},"capacidad":capacidad},
                           "18:00 a 22:00": {"integrantes":{},"capacidad":capacidad}
                           }
    self.ruta = None
    
  
  
  
  
  
  def printInfoArea(self):
    print("Nombre del area de entrenamiento:", self.nombres)
    print('Horarios')
    horarios = self.horarios
    clavesHorarios= list(horarios.keys())
    for i,hora in enumerate(horarios):
        print(f"\t{hora}: \n\t\tIntegrantes: {horarios[hora]['capacidad']}")
  
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
      if self.validarNIntegtrantes(strHorario):
        self.SetearValores(strHorario,integrante)
        with open(ruta_Archivo, "w") as archivo_json:
          json.dump(self.__dict__,archivo_json,indent=4)
  
  def validarNIntegtrantes(self,strHorario):
    if self.horarios[strHorario]["capacidad"] < 33:
      return True
    else: False
    
  def SetearValores(self,strHorario,sujeto):
    integrantes = self.horarios[strHorario]["integrantes"]
    
    if sujeto.documento not in integrantes:
      sujeto.area = self.nombres
      sujeto.horario = strHorario
      crearJson(sujeto,f"{CARPETAS[0]}{sujeto.documento}.json")
      integrantes[sujeto.documento] = sujeto.__dict__
      self.horarios[strHorario]["capacidad"] += 1
    else:
      print('El camper ya esta asignado')





