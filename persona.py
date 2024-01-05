class Persona:
    def __init__(self, documento, nombres, apellidos, telefono, direccion) -> object:
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self. direccion = direccion

class Camper(Persona):
    def __init__(self, documento, nombres, apellidos, 
                 telefono, direccion, acudiente, estado) -> Persona:
        super().__init__(documento, nombres, apellidos, telefono, direccion)
        self.acudiente = acudiente
        self.estado = estado