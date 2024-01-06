from classes.persona import *
class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente, estado='Inscrito', ruta =None) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
        
    def showData(cls):
      """Muestra en un formato legible y ordenado la informacion del objeto, en este caso del Camper
      """
      super().showData()
      print(f'Estado: {cls.estado}\nRuta: {cls.ruta}')
      
      
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
            "ruta": self.ruta
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
            data['estado'],
            data['ruta']
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