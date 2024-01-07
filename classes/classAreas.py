areas = {}
import json
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
  
  def agregarIntegrante(self,integrante):
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]))
    if elec in HORARIOS:
      strHorario = HORARIOS[elec]
      if self.validarNIntegtrantes(strHorario):
        self.SetearValores(strHorario,integrante)
  
  def validarNIntegtrantes(self,strHorario):
    if self.capacidad["horarios"][strHorario]["capacidad"] < 33:
      return True
    else: False
    
  def SetearValores(self,strHorario,integrante):
    self.capacidad["horarios"][strHorario]["integrantes"][integrante.documento] = integrante
    self.capacidad["horarios"][strHorario]["capacidad"] += 1





