from persona import *
class Entrenador(Persona):
    def __init__(self, documento, nombres, apellidos, movil,fijo, direccion, ruta, horario) -> Persona: #Investigar si es necesario esto
        super().__init__(documento, nombres, apellidos, movil,fijo, direccion)
        self.ruta = ruta
        self.horario = horario