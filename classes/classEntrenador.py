# from classes.persona import 
class Entrenador:
  def __init__(self, documento, nombres, apellidos, movil, ruta, horario): #Investigar si es necesario esto
      self.documento = documento
      self.nombres = nombres
      self.apellidos = apellidos
      self.movil = movil
      self.ruta = ruta
      self.horario = horario
      
  @staticmethod
  def solcitarDatosTrainer(RUTAS):
    documento = input("Ingrese el documento: ")
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    movil = input("Ingrese el número de móvil: ")
    numRuta = input(("\n".join([f'{i+1}. {RUTAS[ruta].nombres}' for i,ruta in enumerate(RUTAS)])) + "\nEleccion: ")
    NOMBRERUTAS = list(RUTAS.keys())
    print(NOMBRERUTAS)
    
    HORARIOS = {
    '1': "6:00 a 10:00",
    '2': "10:00 a 14:00",
    '3': "14:00 a 18:00",
    '4': "18:00 a 22:00"}
    elec = input("\n".join([f"{key}. {value}" for key,value in HORARIOS.items()]) + "\nEleccion: ")
    # fijo = input("Ingrese el número fijo: ")
    print(HORARIOS[elec])
    input()
    return documento,nombres,apellidos,movil,NOMBRERUTAS[int(numRuta)-1],HORARIOS[elec]
  
  def showTrainer(self):
    print(f'El trainer {self.nombres} tiene la ruta {self.ruta} con {self.horario}')
    pass
  
  @staticmethod
  def listTrainers(TRAINERS):
    for trainer in TRAINERS:
      trainer.showTrainer()
      input("Presione enter para continuar")
        
    