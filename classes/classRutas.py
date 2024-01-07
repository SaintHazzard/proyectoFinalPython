import json
# from processJsonToMain import *
rutas = {
  
}
class RutaEntrenamiento:
  def __init__(self, nombres = None, modulos = None, sgdbPrincipal=None, sgdbAlternativo=None):
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


class Modulo:
    def __init__(self, nombres, temas):
        self.nombres = nombres
        self.temas = temas
    
    
    def showModulo(self):
      # Siempre retornar str,int u objetos simples para utilizar otro constructor
      return self.temas



