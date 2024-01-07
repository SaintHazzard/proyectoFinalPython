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
    OPCIONES = {
      "1" : "Nota teorica",
      "2" : "Nota practica",
      "3" : "Volver al menu principal"
    }
    while True:
      try:
        ruta_archivo = f"jsonData/{self.documento}.json"
        with open(ruta_archivo, 'r') as archivo_json:
          sujeto = json.load(archivo_json)
        elec=input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\n")
        if elec in OPCIONES:
          if elec == '3':
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
        with open(ruta_archivo,'w') as archivo_json:
          json.dump(sujeto,archivo_json,indent=4)
        if self.notas['nota practica'] and self.notas['nota teorica'] and promedio < 60:
          print(f"El camper ha reprobado la admision con nota promedio de:  {round(promedio,2)}")
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