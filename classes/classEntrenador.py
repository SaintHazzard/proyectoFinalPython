# from classes.persona import 
from processJsonToMain import *
from classes.classAreas import *
class Entrenador:
  def __init__(self, documento = None, nombres = None, apellidos = None, movil= None, rutas= None, horario= None): #Investigar si es necesario esto
      self.documento = documento
      self.nombres = nombres
      self.apellidos = apellidos
      self.movil = movil
      self.rutas = {}
      self.horarios = {}
      
  @staticmethod
  def solcitarDatosTrainer(TRAINERS):
    while True:
      documento = input("Ingrese el documento: ")
      if not documento.isdigit():
        print('Ingrese solo numeros en el numero de documento: ')
        continue
      if documento not in TRAINERS:
        nombres = input("Ingrese los nombres: ")
        apellidos = input("Ingrese los apellidos: ")
        if not nombres.isalpha() and apellidos.isalpha():
          print('Ingrese letras en nombres y apellidos')
          continue
        movil = input("Ingrese el número de móvil: ")
        if not movil.isdigit():
          print('Ingrese solo numero en el numero movil')
          continue
        print('Trainer registrado')
        return documento,nombres,apellidos,movil,
      else:
        print("El documento esta relacionado a otro trainer")
        return list(TRAINERS[documento].__dict__.values())
        
      
    
    
  def setTrainerRutaArea(self,RUTAS,AREAS):
      numRuta = input(("\n".join([f'{i+1}. {RUTAS[ruta].nombres}' for i,ruta in enumerate(RUTAS)])) + "\nEleccion: ")
      NOMBRERUTAS = list(RUTAS.keys())
      # print(NOMBRERUTAS)
      
      HORARIOS = {
      '1': "6:00 a 10:00",
      '2': "10:00 a 14:00",
      '3': "14:00 a 18:00",
      '4': "18:00 a 22:00"}
      
      elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\nEleccion: ")
      # fijo = input("Ingrese el número fijo: ")
      NOMBREAREAS = list(AREAS.keys())
      elecArea = input("\n".join([f"{key+1}. {value}" for key,value in enumerate(NOMBREAREAS)]) + "\nEleccion: ")
      pointTrainerArea = AREAS[NOMBREAREAS[int(elecArea)-1]].horarios[HORARIOS[elec]]
      if pointTrainerArea['Trainer'] is not None:
        print("El Area y horario ya tienen un Trainer asignado")
      if HORARIOS[elec] in self.horarios:
        print(f"El trainer ya tiene ese horario ocupado: {self.horarios}")
        pass
      if pointTrainerArea['Trainer'] is None and len(self.horarios) < 4 and HORARIOS[elec] not in self.horarios:
        self.horarios[HORARIOS[elec]] = AREAS[NOMBREAREAS[int(elecArea)-1]].nombres
        pointTrainerArea['Trainer'] = self.nombres
        pointTrainerArea['rutas'] = NOMBRERUTAS[int(numRuta)-1]
        self.rutas[NOMBRERUTAS[int(numRuta)-1]] = NOMBRERUTAS[int(numRuta)-1]
        pointArea = AREAS[NOMBREAREAS[int(elecArea)-1]]
        crearJson(AREAS[NOMBREAREAS[int(elecArea)-1]],f'{CARPETAS[1]}{pointArea.nombres}.json')
        crearJson(self,f'{CARPETAS[3]}{self.documento}.json')
        # NOMBRERUTAS[int(numRuta)-1],HORARIOS[elec]
        print('Entrenador registrado correctamente en el horario y area')
      

  def showTrainer(self):
    print(f'El trainer {self.documento} {self.nombres} {f"tiene los horarios {self.horarios}" if len(self.horarios) > 0 else "no tiene horarios asignados"}')
    pass
  
  # @staticmethod
  # def listTrainers(TRAINERS):
  #   for trainer in TRAINERS:
  #     trainer.showTrainer()
  #     input("Presione enter para continuar")
        
    