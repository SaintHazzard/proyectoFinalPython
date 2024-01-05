class Persona:
    def __init__(self, documento, nombres, apellidos, telefono, direccion) -> object:
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self. direccion = direccion
    
    def showData(self, registroAspirantes):
         print(f'Documento: {self.documento}\nNombre: {self.nombre}\n Estado: {self.estado}\nRuta: {self.ruta}')

class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, 
                 telefono, direccion, acudiente, estado, ruta) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, telefono, direccion)
        self.acudiente = acudiente
        self.estado = estado
        self.ruta = ruta
        
class Entrenador(Persona):
    def __init__(self, documento, nombres, apellidos, telefono, direccion, ruta, horario) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, telefono, direccion)
        self.ruta = ruta
        self.horario = horario



