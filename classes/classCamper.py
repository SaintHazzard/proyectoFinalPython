from classes.persona import *
from validarValores import *

class Camper(Persona):
  def __init__(self, documento = 0, nombres ='', apellidos='', movil=0, fijo=0, direccion='', acudiente='',
                notaTeorica=None, notaPractica=None, estado='Inscrito', ruta=None) -> Persona:
      """Instanciamiento de Camper"""
      super().__init__(documento, nombres, apellidos, movil, fijo, direccion)
      self.acudiente = acudiente
      self.estado = estado
      self.ruta = ruta
      self.area = None
      self.horario = None
      self.notas = {'nota teorica': notaTeorica or 0, 'nota practica': notaPractica or 0}
      
  def showData(self):
    """Muestra en un formato legible y ordenado la informacion del objeto, en este caso del Camper
    """
    super().showData()
    print(f'Estado: {self.estado}\nRuta: {self.ruta}\nNotas: {self.notas}')

  def getPromedio(self):
    notaTeorica = self.notas['nota teorica']
    notaPractica = self.notas['nota practica'] 
    promedio = (notaTeorica+notaPractica)/2
    return promedio
  
  def getState(self):
    return self.estado
  
  
  def setValoresNota(self,strNota,nota,sujeto):
    self.notas[strNota.lower()] = nota
    sujeto['notas'][strNota] = self.notas[strNota.lower()]

  def setNota(self):
    OPCIONES = {str(i+1): key.capitalize() for i,key in enumerate(self.notas)}
    while True:
      try:
        ruta_archivo = f"jsonData/{self.documento}.json"
        with open(ruta_archivo, 'r') as archivo_json:
          sujeto = json.load(archivo_json)
        elec=input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\n" + "0. Menu principal\n")
        if elec in OPCIONES or elec == "0":
          if elec == '0':
            print('Volviendo al menu principal...')
            break
          strElecNota = OPCIONES[elec].lower()
          nota = int(input(f'Ingrese la {OPCIONES[elec]}: '))
          if value0To100(nota):
            self.setValoresNota(strElecNota,nota,sujeto)
        else:
          input('Opcion no valida, intente de nuevo. Enter para continuar')
          continue
        promedio = self.getPromedio()
        if  promedio >= 60:
          print(f"El camper ha sido aprobado con nota promedio de:  {round(promedio,2)}")
          self.estado = 'Aprobado'
          sujeto['estado'] = self.estado
          # crea un json con el objeto modificado
        if self.notas['nota practica'] and self.notas['nota teorica'] and promedio < 60:
          print(f"El camper ha reprobado la admision con nota promedio de:  {round(promedio,2)}")
        with open(ruta_archivo,'w') as archivo_json:
          json.dump(sujeto,archivo_json,indent=4)
          
        self.setCamperInArea(sujeto)  


      except ValueError as e:
        print(f'El input suministrado es una letra, ingrese un numero')
  

  @staticmethod
  def solicitar_datos_camper():
    documento = input("Ingrese el documento: ")
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    movil = input("Ingrese el número de móvil: ")
    fijo = input("Ingrese el número fijo: ")
    direccion = input("Ingrese la dirección: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    # estado = input("Ingrese el estado: ")
    # ruta = input("Ingrese la ruta: ")
    return documento, nombres, apellidos, movil, fijo, direccion, acudiente


  def setCamperInArea(self,sujeto):
    if self.area is not None:
      ruta_area = f'jsonDataAreas/{self.area}.json'
      with open(ruta_area, 'r') as archivo_json:
        area = json.load(archivo_json)
        point = area['capacidad']['horarios'][f'{sujeto["horario"]}']["integrantes"]
        if self.documento in point:
          point[self.documento] = sujeto
          with open(ruta_area, 'w') as archivo_json:
            json.dump(area,archivo_json,indent=4)


  def verifyAreaCamper(self):
    if self.area is None:
      return True
    print(f'El camper ya tiene el area {self.area} asignada')
    False
    
  def verifyBothCal(self):
    if self.notas['nota teorica'] and self.notas['nota practica']:
      return True
    if not self.notas['nota teorica'] and len(self.notas) == 2:
      print("La nota teorica aun no ha sido registrada")
    if not self.notas['nota practica'] and len(self.notas) == 2:
      print("La nota practica aun no ha sido registrada")
    print('El Camper no tiene todas las notas registradas, no se le puede asignar area')
    return False