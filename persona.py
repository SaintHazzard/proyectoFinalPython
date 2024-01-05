import json
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
         
    def to_JSON(self):
      return{
            "documento": self.documento,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "telefono": self.telefonos,
            "direccion": self.direccion
        }
    def crearJson(self):
        # Ruta del archivo donde guardarás el JSON
      ruta_archivo = f"jsonData/{self.nombres}.json"
      # Guardar los datos como JSON en un archivo
      with open(ruta_archivo, 'w+') as archivo_json:
          json.dump(self.to_JSON(), archivo_json)

      print(f"Datos guardados en {ruta_archivo}")

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
    



