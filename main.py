from classes.persona import * 
from classes.classAreas import *
from classes.classRutas import *

from toolsTest.visuals import *
from processJsonToMain import *
# from crearSujetos import  *
from subMenuRegistro import *
from submenuCamper import *
from submenuareasrutas import *


DATA = {
  
}
RUTAS = {
  
}
AREAS = {
  
}

TRAINERS = {
  
}




menu = "1. Modulo registro\n2. Modulo notas Camper\n3. Modulo administracion areas y rutas\n0. Salir"

if __name__=="__main__":
  
  while True:
    
    clear()
    
    print(menu)
    temporalDatosJson = from_JSOn(CARPETAS[0]);procesarJsonToCamper(Camper,DATA,temporalDatosJson)
    temporalDatosJson = from_JSOn(CARPETAS[1]);procesarJsonToCamper(areasEntrenamiento, AREAS,temporalDatosJson)
    temporalDatosJson = from_JSOn(CARPETAS[2]);procesarJsonToCamper(RutaEntrenamiento,RUTAS,temporalDatosJson)

    elec = input('Eleccion: ')
    if elec == '1':
      submenuregistro(DATA,RUTAS,TRAINERS)
    if elec == '2':
      submenucamper(DATA)
      pass
    elif elec == "3":
      submenuareasyrutas(DATA,AREAS,RUTAS,CARPETAS)
      pass
    if elec == '0':
      ver= input('Esta seguro que desea terminar el programa? S/N ')
      if ver == 's' or ver == 'S':
        break
      elif ver == 'n' or ver == 'N':
        continue