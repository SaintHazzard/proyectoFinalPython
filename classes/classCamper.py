from classes.persona import *
class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente, estado='Inscrito', ruta =None) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
        self.notas = {'nota teorica': 0, 'nota practica': 0}
    
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente,notaTeorica=0,notaPractica=0, estado='Inscrito', ruta =None) -> Persona: 
      """Instanciamiento para convertir de json a objeto
      """
      super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
      self.acudiente = acudiente
      self.estado = estado
      self.ruta = ruta
      self.notas = {'nota teorica': notaTeorica, 'nota practica': notaPractica}
        
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
      ruta_archivo = f"jsonData/{self.nombres}.json"
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
      if self.setState() >= 60:
        # print('Entra')
        self.estado = 'Aprobado'
        sujeto['estado'] = self.estado
        with open(ruta_archivo,'w') as archivo_json:
          json.dump(sujeto,archivo_json,indent=4)
      
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
    def from_dict(cls, data : dict) -> Persona:
      """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
         para ser almacenado en el diccionario del hilo main

      Args:
          data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

      Returns:
          _Camper_: una instancia de la clase @Camper rellenada
      """
      return cls(
            data["documento"],
            data["nombres"],
            data["apellidos"],
            data["telefono"]["movil"],
            data["telefono"]["fijo"],
            data["direccion"],
            data['acudiente'],
            data["notas"]['nota teorica'],
            data["notas"]['nota practica'],
            data["estado"],
            data["ruta"]
        )
      
      
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