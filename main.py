from persona import * 
from visuals import *
from processJsonToMain import *

registroAspirantes = {
  
}
rutas={
  
}

temporalDatosJson = from_JSOn()
procesarJsonToCamper(registroAspirantes,temporalDatosJson)

while True:
  temporalDatosJson = from_JSOn()
  procesarJsonToCamper(registroAspirantes,temporalDatosJson)
  elec = input('Eleccion')
  if elec == '5':
    for documento in registroAspirantes:
      print('-'*50)
      registroAspirantes[documento].showData()