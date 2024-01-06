import json
# from processJsonToMain import *
rutas = {
  
}
class RutaEntrenamiento:
  def __init__(self, nombre, modulos, sgdbPrincipal, sgdbAlternativo):
      self.nombre = nombre
      self.modulos = modulos
      self.sgdbPrincipal = sgdbPrincipal
      self.sgdbAlternativo = sgdbAlternativo
  
  def printRutaEntrenamiento(self):
    print("Nombre de la ruta:", self.nombre)
    print("Modulos")
    for modulo in self.modulos:
        print(f"\t : {', '.join(modulo)}")
    print("SGDB Principal:", self.sgdbPrincipal)
    print("SGDB Alternativo:", self.sgdbAlternativo)
  def showDataRuta(self):
    print(self.nombre)
    print(self.modulos)
    
    
  def crearJson(self):
    # Ruta del archivo donde guardar el JSON
    ruta_archivo = f"jsonDataRutas/{self.nombre}.json"
    print(type(self.modulos))
    with open(ruta_archivo, 'w+') as archivo_json:
        json.dump(self.to_JSON(), archivo_json,indent=4)
    print(f'Ruta registrada satisfactoriamente')
    
    
  @classmethod
  def from_dict(cls, data : dict):
      """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
         para ser almacenado en el diccionario del hilo main

      Args:
          data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

      Returns:
          _Camper_: una instancia de la clase @Camper rellenada
      """
      return cls(
            data['nombre'],
            data['modulos'],
            data["sgdbPrincipal"],
            data['sgdbAlternativo']
        )

class Modulo:
    def __init__(self, nombre, temas):
        self.nombre = nombre
        self.temas = temas
    
    
    def showModulo(self):
      # Siempre retornar str,int u objetos simples para utilizar otro constructor
      return self.temas



