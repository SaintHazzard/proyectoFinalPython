from classes.persona import * 
from toolsTest.visuals import *
from processJsonToMain import *
from crearSujetos import  *


registroAspirantes = {
  
}
rutas={'node': 'Ruta NodeJS', 'java' : 'Ruta Java', 'netcore' : 'Ruta NetCore'}

menu = "1. Registrar Camper\n2. Registrar prueba\n5. Listar personas registradas\n0. Salir"

while True:
  clear()
  print(menu)
  temporalDatosJson = from_JSOn()
  # print(temporalDatosJson)
  procesarJsonToCamper(registroAspirantes,temporalDatosJson)
  # print('*'*50)
  # for documento in registroAspirantes:
  #     print('-'*50)
  #     registroAspirantes[documento].showData()
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
  if elec == '0':
    ver= input('Esta seguro que desea terminar el programa? S/N ')
    if ver == 's' or ver == 'S':
      break
    elif ver == 'n' or ver == 'N':
      continue