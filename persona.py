class Persona:
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion) -> object:
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefonos = {'movil': movil,
                          'fijo': fijo}
        self. direccion = direccion
    def getNombreCompleto(self) -> str:
      return f'{self.nombres} {self.apellidos}'
    
    def showData(self):
         print(f'Documento: {self.documento}\nNombre: {self.nombres}\nApellidos: {self.apellidos}\nTelefonos: \n\tMovil: {self.telefonos["movil"]}\n\tFijo: {self.telefonos["fijo"]}')

class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, acudiente, estado, ruta) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
    def showData(self):
      super().showData()
      print(f'Estado: {self.estado}\nRuta: {self.ruta}')
        
class Entrenador(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, ruta, horario) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.ruta = ruta
        self.horario = horario
    



