from classes.persona import *
from validarValores import *

class Camper(Persona):
  def __init__(self, documento = 0, nombres ='', apellidos='', movil=0, fijo=0, direccion='', acudiente='',
                notaTeorica=None, notaPractica=None, estado='Inscrito', ruta=None) -> Persona:
      """Instanciamiento de Camper"""
      super().__init__(documento, nombres, apellidos, movil, fijo, direccion)
      self.acudiente = acudiente
      self.estado = estado
      self.ruta = {}
      self.area = None
      self.horario = None
      self.notas = {'nota teorica': notaTeorica or 0, 'nota practica': notaPractica or 0}
      self.notasHistory = {}
      self.riesgo = None
      
  def showData(self):
    """Muestra en un formato legible y ordenado la informacion del objeto, en este caso del Camper
    """
    if self.estado == 'Inscrito':
      super().showData()
      print(f'Estado: {self.estado}\nRuta: {self.ruta}\nNotas: {self.notas}')

    
  def showDataAprobado(self):
     if self.estado == 'Aprobado':
      super().showData()
      print(f'Estado: {self.estado}\nRuta: {self.ruta["nombres"]}\nNotas: {self.notas}')

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
        if  promedio >= 60 and len(self.notas) == 2:
          print(f"El camper ha sido aprobado con nota promedio de:  {round(promedio,2)}")
          self.notas['nota final'] = promedio
          self.notasHistory["admision"] = self.notas
          # print(self.notasHistory)
          # print(self.notasHistory["admision"], "aca")
          input("Esperar")
          self.estado = 'Aprobado'
          sujeto['estado'] = self.estado
          sujeto['notasHistory']['admision'] = self.notasHistory["admision"]
          # crea un json con el objeto modificado
        if self.notas['nota practica'] and self.notas['nota teorica'] and promedio < 60 and len(self.notas) == 2:
          print(f"El camper ha reprobado la admision con nota promedio de:  {round(promedio,2)}")
        if len(self.notas) == 4 and self.notas["nota teorica"] and self.notas["nota practica"] and self.notas["nota trabajo"] and self.notas["nota quices"]:
          print("A que modulo desea agregar notas las notas: ")
          OPCIONESMODULOS = {str(i+1): key.capitalize() for i,key in enumerate(self.ruta['modulos'])}
          elecMod=input("\n".join([f'{key}. {value}' for key,value in OPCIONESMODULOS.items()]) + "\n" + "0. Menu principal\n")
          # print(elecMod, "elecmod")
          print('Seleccione submodulo')
          if elecMod is "0":
            break
          elecDetail=input("\n".join([f'{key+1}. {value}' for key,value in enumerate(self.ruta['modulos'][OPCIONESMODULOS[elecMod].lower()])]) + "\n" + "0. Menu principal\n")
          SUBMODULOS = self.ruta['modulos'][OPCIONESMODULOS[elecMod].lower()]
          promedio = self.getPromedio()
          # self.notas['nota final'] = promedio
          
          
          teorica = self.notas["nota teorica"] * 0.3
          practica = self.notas["nota practica"] * 0.6
          otros = (self.notas["nota trabajo"] + self.notas["nota quices"]) / 2 * 0.1
          notafinal = teorica + practica + otros
          self.notas['nota final'] = notafinal
          sujeto['notasHistory'][SUBMODULOS[int(elecDetail)-1]] = self.notas
          if notafinal < 60:
            sujeto["riesgo"] = 'Alto'
            self.riesgo = 'Alto'
          else: sujeto['riesgo'] ='Bajo'; self.riesgo = 'Bajo'
          sujeto['notas'] = {key : 0 for key in sujeto['notas']}
          self.notas = {key : 0 for key in self.notas}
          print(f'La nota final del camper en el submodulo {SUBMODULOS[int(elecDetail)-1]} fue {notafinal}')
        with open(ruta_archivo,'w+') as archivo_json:
          json.dump(sujeto,archivo_json,indent=4)
        
          
          
        # self.setCamperInArea(sujeto)  


      except ValueError as e:
        print(f'El input suministrado es una letra, ingrese un numero')
  

  @staticmethod
  def solicitar_datos_camper(data):
    while True:
      documento = input("Ingrese el documento: ")
      if documento in data:
        print('Ya hay un camper registrado con este documento')
        continue
      if not documento.isdigit():
        print('Ingrese un numero trolazo')
        continue
      nombres = input("Ingrese los nombres: ")
      apellidos = input("Ingrese los apellidos: ")
      if not apellidos.isalpha() or not nombres.isalpha():
        print('Datos en nombres y apellidos incorrectos porque contiene numeros')
        continue
      movil = input("Ingrese el número de móvil: ")
      fijo = input("Ingrese el número fijo: ")
      if not movil.isdigit() and not fijo.isdigit():
        print("Valos ingresados en movil o fijo no validos")
        continue
      direccion = input("Ingrese la dirección: ")
      acudiente = input("Ingrese el nombre del acudiente: ")
      if not acudiente.isalpha():
        print('Ingrese nombre del acudiente correctamente')
        continue
      # estado = input("Ingrese el estado: ")
      # ruta = input("Ingrese la ruta: ")
      return documento, nombres, apellidos, movil, fijo, direccion, acudiente


  def setCamperInArea(self,sujeto):
    if self.area is not None:
      ruta_area = f'jsonDataAreas/{self.area}.json'
      with open(ruta_area, 'r') as archivo_json:
        area = json.load(archivo_json)
        point = area['horarios'][f'{sujeto["horario"]}']["integrantes"]
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
    if self.notas['nota teorica'] and self.notas['nota practica'] and len(self.notas) == 2:
      return True
    if not self.notas['nota teorica'] and len(self.notas) == 2:
      print("La nota teorica aun no ha sido registrada")
    if not self.notas['nota practica'] and len(self.notas) == 2:
      print("La nota practica aun no ha sido registrada")
    # print('El Camper no tiene todas las notas registradas, no se le puede asignar area')
    return False