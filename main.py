from classes.persona import * 
from toolsTest.visuals import *
from processJsonToMain import *

registroAspirantes = {
  
}
rutas={
  
}



while True:
  temporalDatosJson = from_JSOn()
  procesarJsonToCamper(registroAspirantes,temporalDatosJson)
  elec = input('Eleccion')
  if elec == '5':
    for documento in registroAspirantes:
      print('-'*50)
      registroAspirantes[documento].showData()