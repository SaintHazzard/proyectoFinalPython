from classes.persona import *
class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil, fijo, direccion, acudiente,
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
      ruta_archivo = f"jsonData/{self.documento}.json"
      with open(ruta_archivo, 'r') as archivo_json:
        sujeto = json.load(archivo_json)
      elec=input('Se puede registrar nota, que nota desea registrar\n\t1. Nota teorica\n\t2. Nota practica\n')
      if elec == '1':
        self.notas['nota teorica'] = int(input('Ingrese la nota teorica: '))
        sujeto['notas']['nota teorica'] = self.notas['nota teorica']
      if elec == '2':
        self.notas['nota practica'] = int(input('Ingrese la nota practica: '))
        sujeto['notas']['nota practica'] = self.notas['nota practica']
      with open(ruta_archivo,'w') as archivo_json:
        json.dump(sujeto,archivo_json,indent=4)
      print('Nota registrada')
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
    # crea un json con el objeto
    
    def to_JSON(self):
       return{
            "documento": self.documento,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "telefono": self.telefonos,
            "direccion": self.direccion,
            "acudiente": self.acudiente,
            "estado": self.estado,
            "ruta": self.ruta,
            "notas": self.notas
        }
       
       
    # clc es como decir Camper(relleno), es decir instancia la clase con el argumento @data que se le suministra
    @classmethod
    def from_dict(self, data : dict) -> Persona:
      """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
         para ser almacenado en el diccionario del hilo main

      Args:
          data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

      Returns:
          _Camper_: una instancia de la clase @Camper rellenada
      """
      for clave, valor in data.items():
            setattr(self, clave, valor)
      
      
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