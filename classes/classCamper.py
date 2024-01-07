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

    def setState(self):
      notaTeorica = self.notas['nota teorica']
      notaPractica = self.notas['nota practica'] 
      # print(notaTeorica,notaPractica)
      promedio = (notaTeorica+notaPractica)/2
      # print(promedio)
      return promedio
    
    def getState(self):
      return self.estado
    
    def setNota(self):
      while True:
        try:
          ruta_archivo = f"jsonData/{self.documento}.json"
          with open(ruta_archivo, 'r') as archivo_json:
            sujeto = json.load(archivo_json)
          elec=input('Se puede registrar nota, que nota desea registrar\n\t1. Nota teorica\n\t2. Nota practica\n\t3. Volver al menu principal\n\t')
          if elec not in ['1','2','3']:
            continue
          if elec == '1':
            nota = int(input('Ingrese la nota teorica: '))
            if value0To100(nota):
              self.notas['nota teorica'] = nota
            sujeto['notas']['nota teorica'] = self.notas['nota teorica']
            
            
            
            
          if elec == '2':
            nota = int(input('Ingrese la nota practica: '))
            if value0To100(nota):
              self.notas['nota practica'] = nota
              sujeto['notas']['nota practica'] = self.notas['nota practica']
              
              
              
              
          if elec == '3':
            break
          with open(ruta_archivo,'w') as archivo_json:
            json.dump(sujeto,archivo_json,indent=4)
          
          # print(self.nombres)
          promedio = self.setState()
          if  promedio >= 60:
            print(f"El camper ha sido aprobado con nota promedio de:  {round(promedio,2)}")
            self.estado = 'Aprobado'
            sujeto['estado'] = self.estado
            with open(ruta_archivo,'w') as archivo_json:
              json.dump(sujeto,archivo_json,indent=4)
          if self.notas['nota practica'] and self.notas['nota teorica'] and promedio < 60:
            print(f"El camper ha reprobado la admision con nota promedio de:  {round(promedio,2)}")
        except ValueError as e:
          print(f'El input suministrado es una letra, ingrese un numero')
    # crea un json con el objeto
    
    
       
      
      
    @classmethod
    def solicitar_datos_camper(cls):
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