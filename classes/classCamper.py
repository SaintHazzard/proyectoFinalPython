from classes.persona import *
class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente, estado, ruta) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
    def showData(self):
      super().showData()
      print(f'Estado: {self.estado}\nRuta: {self.ruta}')
      
      
      
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
    @classmethod
    def from_dict(cls, data):
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