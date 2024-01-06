from classes.persona import * 
from toolsTest.visuals import *
from processJsonToMain import *
from crearSujetos import  *
from classes.classAreas import *
from classes.classRutas import *


registroAspirantes = {
  
}
rutasExistentes = {
  
}
areas = {
  
}

CARPETAS = ['jsonData/','jsonDataAreas/','jsonDataRutas/']

menu = "1. Registrar Camper\n2. Registrar prueba\n5. Listar personas registradas\n6. Listar rutasExistentes\n7. Listar areas de entrenamiento\n0. Salir"

while True:
  
  clear()
  
  print(menu)
  # for carpeta in CARPETAS:
  temporalDatosJson = from_JSOn(CARPETAS[0]);procesarJsonToCamper(Camper,registroAspirantes,temporalDatosJson)
  temporalDatosJson = from_JSOn(CARPETAS[1]);procesarJsonToCamper(areasEntrenamiento, areas,temporalDatosJson)
  temporalDatosJson = from_JSOn(CARPETAS[2]);procesarJsonToCamper(RutaEntrenamiento,rutasExistentes,temporalDatosJson)
  # procesarJsonToCamper(rutasExistentes,)
  print(rutasExistentes)
  elec = input('Eleccion: ')
  if elec == '1':
    documentoCamper,*demasDatos=Camper.solicitar_datos_camper()
    registroAspirantes[documentoCamper] = Camper(documentoCamper,*demasDatos)
    registroAspirantes[documentoCamper].crearJson()
    wait()
  if elec == '2':
    documento=input('Documento del camper a registrar nota: ')
    print()
    if registroAspirantes[documento].getState() == 'Inscrito':
      registroAspirantes[documento].setNota()
    else: print(f"Solo puede registrar nota de campers son el estado de 'Inscrito' y el estado del camper con documento {documento} es {registroAspirantes[documento].getState()}")
    wait()
    pass
  if elec == '5':
    for documento in registroAspirantes:
      print('-'*50)
      registroAspirantes[documento].showData()
    wait()
  if elec=='6':
    for ruta in rutasExistentes:
      print('-'*50)
      print(ruta)
      rutasExistentes[ruta].printRutaEntrenamiento()
      
    wait()
    pass
  if elec=='7':
    for area in areas:
      print('-'*50)
      areas[area].printInfoArea()
      input('Esperar')
    wait()
    pass
  if elec == '0':
    ver= input('Esta seguro que desea terminar el programa? S/N ')
    if ver == 's' or ver == 'S':
      break
    elif ver == 'n' or ver == 'N':
      continue