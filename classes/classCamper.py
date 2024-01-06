from classes.persona import *
class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente, estado, ruta) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
        
        
        
    @classmethod
    def showData(self):
      """Muestra en un formato legible y ordenado la informacion del objeto, en este caso del Camper
      """
      super().showData()
      print(f'Estado: {self.estado}\nRuta: {self.ruta}')
      
      
    # crea un json con el objeto
    @classmethod
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