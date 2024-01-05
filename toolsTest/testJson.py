registroAspirantes = {
  
}
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
    
    def to_JSON(self):
          return {
                "documento": self.documento,
                "nombres": self.nombres,
                "apellidos": self.apellidos,
                "telefono": self.telefonos,
                "direccion": self.direccion
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
          


registroAspirantes['0']= Persona('1091356862', 'Sofia Marcela', 'Medina Diaz',3165880900,123123456 , 'Cir 36a 104-128 Altos de la Pradera T3-1204')


aspirante0 = registroAspirantes['0'].to_JSON()
aspirante0_objeto=Persona.from_dict(aspirante0)


print(aspirante0_objeto)

# print(aspirante0)