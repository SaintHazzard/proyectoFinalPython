import json
# from processJsonToMain import *
rutas = {
  
}
class RutaEntrenamiento:
  def __init__(self, nombres, modulos, sgdbPrincipal, sgdbAlternativo):
      self.nombres = nombres
      self.modulos = modulos
      self.sgdbPrincipal = sgdbPrincipal
      self.sgdbAlternativo = sgdbAlternativo
  
  def printRutaEntrenamiento(self):
    print("Nombre de la ruta:", self.nombres)
    print("Modulos")
    for modulo in self.modulos:
        print(f"\t : {', '.join(modulo)}")
    print("SGDB Principal:", self.sgdbPrincipal)
    print("SGDB Alternativo:", self.sgdbAlternativo)
    
  def to_JSON(self):
       return{
            "nombres": self.nombres,
            "modulos": self.modulos,
            "sgdbPrincipal": self.sgdbPrincipal,
            "sgdbAlternativo": self.sgdbAlternativo,
        }
    
    
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
            data['nombres'],
            data['modulos'],
            data["sgdbPrincipal"],
            data['sgdbAlternativo']
        )

class Modulo:
    def __init__(self, nombres, temas):
        self.nombres = nombres
        self.temas = temas
    
    
    def showModulo(self):
      # Siempre retornar str,int u objetos simples para utilizar otro constructor
      return self.temas



