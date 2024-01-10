areas = {}
import json
import os
from processJsonToMain import *
# from classRutas import *
class areasEntrenamiento:
  def __init__(self,nombres=None,capacidad=0,ruta=None) -> object:
    self.nombres = nombres
    # self.ruta = ''
    self.horarios = {"6:00 a 10:00":{"integrantes":{},"capacidad":capacidad, "ruta" : ruta ,"Trainer": None}, 
                           "10:00 a 14:00": {"integrantes":{},"capacidad":capacidad, "ruta" : ruta,"Trainer": None},
                           "14:00 a 18:00": {"integrantes":{},"capacidad":capacidad, "ruta" : ruta,"Trainer": None},
                           "18:00 a 22:00": {"integrantes":{},"capacidad":capacidad, "ruta" : ruta,"Trainer": None}
                           }
    
  
  
  def printInfoArea(self):
    print("Nombre del area de entrenamiento:", self.nombres)
    print('Horarios')
    horarios = self.horarios
    clavesHorarios= list(horarios.keys())
    for i,hora in enumerate(horarios):
        print(f"\t{hora}: \n\t\tIntegrantes: {horarios[hora]['capacidad']}")
  
  def agregarIntegrante(self,integrante,carpeta,RUTAS):
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    print('Indique el horario: ')
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\nEleccion: ")
    if elec in HORARIOS:
      ruta_Archivo = f'{carpeta}{self.nombres}.json'
      # with open(ruta_Archivo, 'r') as archivo_json:
      #   area = json.load(archivo_json)
      strHorario = HORARIOS[elec]
      if self.validarNIntegtrantes(strHorario):
        self.SetearValores(strHorario,integrante,RUTAS)
        with open(ruta_Archivo, "w") as archivo_json:
          json.dump(self.__dict__,archivo_json,indent=4)
  
  def validarNIntegtrantes(self,strHorario):
    if self.horarios[strHorario]["capacidad"] < 33:
      return True
    else: False
    
  def SetearValores(self,strHorario,sujeto,RUTAS):
    integrantes = self.horarios[strHorario]["integrantes"]
    
    if sujeto.documento not in integrantes:
      nombreRuta = self.horarios[strHorario]['rutas']
      sujeto.ruta = RUTAS[nombreRuta].__dict__
      sujeto.area = self.nombres
      sujeto.horario = strHorario
      sujeto.notas['nota trabajo'] = 0
      sujeto.notas['nota quices'] = 0
      # sujeto.ruta = self.horarios[strHorario]['rutas']
      sujeto.notas = {key: 0 for key in sujeto.notas}
      reInstanciar(Camper,sujeto.__dict__)
      crearJson(sujeto,f"{CARPETAS[0]}{sujeto.documento}.json")
      individuo = sujeto.__dict__
      integrantes[sujeto.documento] = f"{individuo['nombres']} {individuo['apellidos']}"
      # integrantes[sujeto.nombres][integrantes[sujeto.documento]] = individuo['nombres']
      self.horarios[strHorario]["capacidad"] += 1
    else:
      print('El camper ya esta asignado')
  
  def setRuta(self,rutasExistentes,integrantes):
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    # rutasJson = list(from_JSOn(CARPETAS[2]).keys())
    print('Que ruta desea agregar al area :')
    temporalDatosJson = from_JSOn(CARPETAS[2]);procesarJsonToCamper(RutaEntrenamiento,rutasExistentes,temporalDatosJson)
    numRuta = input(("\n".join([f'{i+1}. {rutasExistentes[ruta].nombres}' for i,ruta in enumerate(rutasExistentes)])) + "\nEleccion: ")
    rutasJson = list(rutasExistentes.keys())
    print(rutasExistentes)
    print(rutasJson)
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\n")
    if elec in HORARIOS:
      strHorario = HORARIOS[elec]
    # with open()
    rutaSeleccionada = rutasExistentes[rutasJson[int(numRuta)-1]]
    self.horarios[strHorario]["ruta"] = rutaSeleccionada.__dict__["nombres"]
    
    dictIntegrantesArea = self.horarios[strHorario]["integrantes"]
    for key,value in integrantes.items():
      doc = value.__dict__["documento"]
      if doc in dictIntegrantesArea:
        
        crearJson(reInstanciar(Camper,value.__dict__),(f'jsonData/{value.__dict__["documento"]}.json'))
    crearJson(self,(f'{CARPETAS[1]}{self.nombres}.json'))
    print(f'Ruta {rutasJson[int(numRuta)-1]} agregada al area {self.nombres} en el horario {strHorario}')

      
      

      
# FROMJSON SI O SI
      
      






