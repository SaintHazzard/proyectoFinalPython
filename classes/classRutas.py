import json
# from processJsonToMain import crearJson

from classes.processJsonToMain import *

class RutaEntrenamiento:
  def __init__(self, nombres=None, modulos=None, sgdbPrincipal=None, sgdbAlternativo=None):
      self.nombres = nombres
      self.modulos = modulos or {}
      self.sgdbPrincipal = sgdbPrincipal
      self.sgdbAlternativo = sgdbAlternativo

  def printRutaEntrenamiento(self):
      print("Nombre de la ruta:", self.nombres)
      print("Modulos")
      for modulo in self.modulos.values():
          print(f"\t : {', '.join(modulo)}")
      print("SGDB Principal:", self.sgdbPrincipal)
      print("SGDB Alternativo:", self.sgdbAlternativo)

  @classmethod
  def crearRuta(cls, nombreRuta):
      ruta = cls(nombreRuta)
      crearJson(ruta, f"jsonDataRutas/{ruta.nombres}.json")
      MODULOS = {
          "fundamentos": Modulo("Fundamentos de programación", ["Introducción a la algoritmia", "PSeInt", "Python"]).getModulo(),
          "web": Modulo("Programación Web", ["HTML", "CSS", "Bootstrap"]).getModulo(),
          "formal": Modulo("Programación formal", ["Java", "JavaScript", "C#"]).getModulo(),
          "backend": Modulo("Backend", ["NetCore", "Spring Boot", "NodeJS", "Express"]).getModulo(),
      }
      ruta.modulos = agregarModulos(MODULOS)
      seleccionarDbs(ruta)
      return ruta
    
  @classmethod
  def seleccionarRuta(cls,rutasExistentes):
    for i in rutasExistentes:
      print(i)
      print('entra')
    pass
  



def imprimirModulos(MODULOS):
    print("\n".join([f'{key+1}. Modulo {value.capitalize()}: {", ".join(MODULOS[value])}' for key, value in enumerate(MODULOS)]) + "\n5. Seleccionar base de datos y guardar ruta\n")

def imprimirDbs(dbs):
    for i, value in enumerate(dbs):
        print(f'{i+1}. Base de datos {value}')

def seleccionUsuario(lenElegir):
    while True:
        try:
            if isinstance(lenElegir, dict):
                print("Que modulo desea agregar a la ruta? ")
                imprimirModulos(lenElegir)
            if isinstance(lenElegir, list):
                imprimirDbs(lenElegir)
            nRuta = int(input())

            if 1 <= nRuta <= len(lenElegir)+1 or nRuta == 5:
                return nRuta
            else:
                print("Opcion invalida. Por favor ingrese un numero valido")
        except ValueError as e:
            print("Opción inválida. Por favor, ingrese un número válido.")

def agregarModulos(MODULOS):
    ruta_modulos = {}
    MODULOSNAME = list(MODULOS.keys())

    while True:
        nRuta = seleccionUsuario(MODULOS)
        moduloSeleccionado = MODULOSNAME[nRuta-1] if nRuta <= len(MODULOSNAME) else None

        if moduloSeleccionado in MODULOS:
            if moduloSeleccionado not in ruta_modulos:
                # print(MODULOS[moduloSeleccionado])
                
                ruta_modulos[moduloSeleccionado]=MODULOS[moduloSeleccionado]
                # print(ruta_modulos)
                # input()
                MODULOS.pop(moduloSeleccionado)
                MODULOSNAME.remove(moduloSeleccionado)
                print(f'\t\tModulo {moduloSeleccionado.capitalize()} agregado')
            else:
                print(f'{"-"*20}El modulo ya esta en la ruta{"-"*20}')
            input('Presione enter para continuar')

        if nRuta == 5:
            break

    return ruta_modulos

def seleccionarDbs(ruta):
    dbs = ["MySQL", "MongoDB", "PostgreSQL"]
    while True:
        print('Seleccione base de datos principal')
        # imprimirDbs(dbs)
        db_principal = seleccionUsuario(dbs)

        if 0 <= db_principal < len(dbs)+1:
            ruta.sgdbPrincipal = dbs.pop(db_principal-1)
            break
        else:
            print('Selección inválida. Intente de nuevo.')

    while True:
        print('Seleccione base de datos alternativa')
        # imprimirDbs(dbs)
        db_alternativa = seleccionUsuario(dbs)
        if 0 <= db_alternativa < len(dbs)+1:
            ruta.sgdbAlternativo = dbs.pop(db_alternativa-1)
            break
        else:
            print('Selección inválida. Intente de nuevo.')
    crearJson(ruta, f"jsonDataRutas/{ruta.nombres}.json")
          

# RutaEntrenamiento.seleccionarRuta()
class Modulo:
    def __init__(self, nombres, temas): 
        self.nombres = nombres
        self.temas = temas
    
    
    def getModulo(self):
      # Siempre retornar str,int u objetos simples para utilizar otro constructor
      return self.temas

# newInstanciaRuta = RutaEntrenamiento.crearRuta("Ruta test")
# print(**paquete)
# x = RutaEntrenamiento.crearRuta("Ruta test",*paquete)

# reInstanciar(RutaEntrenamiento,paquete)
# rutas[newInstanciaRuta.nombres] = newInstanciaRuta.__dict__

# print(rutas[newInstanciaRuta.nombres])
# rutas[x.nombres] = x

# print(rutas[x.nombres].__dict__)


