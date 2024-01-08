areas = {}
import json
import os
from processJsonToMain import *
# from classRutas import *
class areasEntrenamiento:
  def __init__(self,nombres=None,capacidad=0) -> object:
    self.nombres = nombres
    # self.ruta = ''
    self.horarios = {"6:00 a 10:00":{"integrantes":{},"capacidad":capacidad, "ruta" : None}, 
                           "10:00 a 14:00": {"integrantes":{},"capacidad":capacidad, "ruta" : None},
                           "14:00 a 18:00": {"integrantes":{},"capacidad":capacidad, "ruta" : None},
                           "18:00 a 22:00": {"integrantes":{},"capacidad":capacidad, "ruta" : None}
                           }
    
  
  
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
  
  def setRuta(self,rutasExistentes):
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    rutasJson = list(from_JSOn(CARPETAS[2]).keys())
    print('Que ruta desea agregar al area :')
    numRuta = input(("\n".join([f'{i+1}. {rutasExistentes[ruta].nombres}' for i,ruta in enumerate(rutasExistentes)])) + "\nEleccion: ")
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\n")
    if elec in HORARIOS:
      strHorario = HORARIOS[elec]
    # with open()
    rutaSeleccionada = rutasExistentes[rutasJson[int(numRuta)-1]]
    self.horarios[strHorario]["ruta"] = rutaSeleccionada.__dict__["nombres"]
    dictIntegrantesArea = self.horarios[strHorario]["integrantes"]
    for i,integrante in dictIntegrantesArea.items():
      dictIntegrantesArea[i]["ruta"] = rutaSeleccionada.nombres
      print(dictIntegrantesArea[i])
      crearJson(reInstanciar(Camper,dictIntegrantesArea[i]),(f'jsonData/{dictIntegrantesArea[i]["documento"]}.json'))
    input('Esperar')
    crearJson(self,(f'{CARPETAS[1]}{self.nombres}.json'))
    input(f'Ruta {rutasJson[int(numRuta)-1]} agregada al area {self.nombres} en el horario {strHorario}')

      
      

      
# FROMJSON SI O SI
      
      






