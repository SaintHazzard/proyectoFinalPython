
from toolsTest.visuals import *
from classes.classCamper import *
from processJsonToMain import *
from classes.classEntrenador import *
from classes.classEntrenador import *
from classes.classEntrenador import *

def submenuregistro(data,RUTAS,trainers):
  OPCIONES ={
    '1' : "Registro Camper",
    "2" : "Registro Docente",
    "0" : "Menu anterior"
  }
  while True:
    elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
    if elec is "1":
      documentoCamper,*demasDatos=Camper.solicitar_datos_camper()
      data[documentoCamper] = Camper(documentoCamper,*demasDatos)
      crearJson(data[documentoCamper],f"{CARPETAS[0]}{documentoCamper}.json")
      wait()
      pass
    elif elec is "2":
      documentoTrainer,*demasDatos=Entrenador.solcitarDatosTrainer(RUTAS)
      trainers[documentoTrainer] = Entrenador(documentoTrainer,*demasDatos)
      crearJson(trainers[documentoTrainer],f"{CARPETAS[3]}{documentoTrainer}.json")
      wait()
      pass
    elif elec is "0":
      break
    elif elec is "2":
      
      pass
  

