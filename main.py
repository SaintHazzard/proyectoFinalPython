from classes.persona import * 
from toolsTest.visuals import *
from processJsonToMain import *
from classes.classCamper import *

registroAspirantes = {
  
}
rutas={
  
}

class Persona:
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion) -> object:
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefonos = {'movil': movil,
                          'fijo': fijo}
        self. direccion = direccion
    def getNombreCompleto(self) -> str:
      return f'{self.nombres} {self.apellidos}'
    
    def showData(self):
         print(f'Documento: {self.documento}\nNombre: {self.nombres}\nApellidos: {self.apellidos}\nTelefonos: \n\tMovil: {self.telefonos["movil"]}\n\tFijo: {self.telefonos["fijo"]}')
         
    
    def crearJson(self):
        # Ruta del archivo donde guardarás el JSON
      ruta_archivo = f"jsonData/{self.nombres}.json"
      # Guardar los datos como JSON en un archivo
      with open(ruta_archivo, 'w+') as archivo_json:
          json.dump(self.to_JSON(), archivo_json,indent=4)

      print(f"Datos guardados en {ruta_archivo}")

while True:
  temporalDatosJson = from_JSOn()
  procesarJsonToCamper(registroAspirantes,temporalDatosJson)
  elec = input('Eleccion')
  if elec == '5':
    for documento in registroAspirantes:
      print('-'*50)
      registroAspirantes[documento].showData()