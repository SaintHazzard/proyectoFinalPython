
from toolsTest.visuals import *
from classes.classCamper import *
from processJsonToMain import *
from classes.classEntrenador import *
from classes.classEntrenador import *
from classes.classEntrenador import *

def submenuregistro(data,TRAINERS):
  OPCIONES ={
    '1' : "Registro Camper",
    "2" : "Registro Docente",
    "0" : "Menu anterior"
  }
  while True:
    print()
    clear()
    elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
    if elec is "1":
      valCamper = Camper.solicitar_datos_camper(data,TRAINERS)
      if valCamper is not None:
        documentoCamper,*demasDatos=valCamper
        data[documentoCamper] = Camper(documentoCamper,*demasDatos)
        crearJson(data[documentoCamper],f"{CARPETAS[0]}{documentoCamper}.json")
        wait()
      else: continue
      pass
    elif elec is "2":
      print()
      trainer = Entrenador.solcitarDatosTrainer(TRAINERS,data)
      if trainer is not None:
        documentoTrainer,*demasDatos= trainer
        for i,k in TRAINERS.items():
          print(i,k)
        if documentoTrainer not in TRAINERS:
          TRAINERS[documentoTrainer] = Entrenador(documentoTrainer,*demasDatos)
          crearJson(TRAINERS[documentoTrainer],f"{CARPETAS[3]}{documentoTrainer}.json")
          input("Entra aca")
          temporalDatosJson = from_JSOn(CARPETAS[3]);procesarJsonToCamper(Entrenador,TRAINERS,temporalDatosJson)
      wait()
      pass
    elif elec is "0":
      break
    elif elec is "2":
      
      pass
  

