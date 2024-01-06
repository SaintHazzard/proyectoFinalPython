from classes.persona import * 
from toolsTest.visuals import *
from processJsonToMain import *


registroAspirantes = {
  
}
rutas={
  
}
menu = "1. Registrar Camp\n2. Registrar prueba\n5. Listar personas registradas"

while True:
  print(menu)
  temporalDatosJson = from_JSOn()
  procesarJsonToCamper(registroAspirantes,temporalDatosJson)
  elec = input('Eleccion: ')
  if elec == '1':
    documentoCamper,*demasdatos=Camper.solicitar_datos_camper(registroAspirantes)
    registroAspirantes[documentoCamper] = Camper(*demasdatos)
    pass
  if elec == '5':
    for documento in registroAspirantes:
      print('-'*50)
      registroAspirantes[documento].showData()