import json
rutas = {
  
}
class RutaEntrenamiento:
  def __init__(self, nombre, modulos, sgdbPrincipal, sgdbAlternativo):
      self.nombre = nombre
      self.modulos = {"modulos" : modulos}
      self.sgdbPrincipal = sgdbPrincipal
      self.sgdbAlternativo = sgdbAlternativo
  @classmethod
  def printRutaEntrenamiento(cls,ruta,modulo):
    print("Nombre de la ruta:", ruta.nombre)
    for modulo in ruta.modulos:
        print(f"- {modulo.nombre}: {', '.join(modulo.temas)}")
    print("SGDB Principal:", ruta.sgdbPrincipal)
    print("SGDB Alternativo:", ruta.sgdbAlternativo)
  def showDataRuta(self):
    print(self.nombre)
    print(self.modulos)
    
    
  def crearJson(self):
      # Ruta del archivo donde guardarás el JSON
    ruta_archivo = f"jsonDataRutas/{self.nombre}.json"
    print(type(self.modulos))
    # print(self.modulos['modulos'][0].showModulo())
    # self.showDataRuta()
    # for i,k in enumerate(self.modulos["modulos"]):
    #   print(type(k.temas))
    #   print(k.temas)
    # print(self.modulos)
    # print(Modulo.showModulo(self.modulos))
    # Guardar los datos como JSON en un archivo
    with open(ruta_archivo, 'w+') as archivo_json:
        json.dump(self.to_JSON(), archivo_json,indent=4)
    # # print(f"Datos guardados en {ruta_archivo}")
    # print(f'Ruta registrada satisfactoriamente')
    
    
  def to_JSON(self):
    return{
          "nombre": self.nombre,
          "modulos": self.modulos,
          "sgdbPrincipal" : self.sgdbPrincipal,
          "sgdbAlternativo" : self.sgdbAlternativo,
      }

class Modulo:
    def __init__(self, nombre, temas):
        self.nombre = nombre
        self.temas = temas
    
    
    def showModulo(self):
      # Siempre retornar str,int u objetos simples para utilizar otro constructor
      return self.temas



modfundamentos = Modulo("Fundamentos de programación", ["Introducción a la algoritmia", "PSeInt", "Python"]).showModulo()
modweb = Modulo("Programación Web", ["HTML", "CSS", "Bootstrap"]).showModulo()
modformal = Modulo("Programación formal", ["Java", "JavaScript", "C#"]).showModulo()
modbd = Modulo("Bases de datos", ["MySQL", "MongoDB", "PostgreSQL"]).showModulo()
modbackend = Modulo("Backend", ["NetCore", "Spring Boot", "NodeJS", "Express"]).showModulo()


rutas["Programación Web"] = RutaEntrenamiento("Programación Web", [modfundamentos, modweb], "MySQL", "MongoDB")
rutas["Desarrollo Backend"] = RutaEntrenamiento("Desarrollo Backend", [modfundamentos, modweb, modformal, modbd, modbackend], "PostgreSQL", "MongoDB")

for i,k in enumerate(rutas):
  rutas[k].crearJson()
  
# RutaEntrenamiento.printRutaEntrenamiento(rutas["Desarrollo Backend"],[modfundamentos, modweb])