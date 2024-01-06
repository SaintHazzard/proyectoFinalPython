import json
class ObjetoDesdeDiccionario:
    def __init__(self, diccionario):
        for clave, valor in diccionario.items():
            setattr(self, clave, valor)

# Ejemplo de uso
diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemploville'}
objeto = ObjetoDesdeDiccionario(diccionario)

# print(dir(objeto))


class Ejemplo:
  def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c

  def mostrar_datos(self):
      print(f'{self.a}...{self.b}...{self.c}')
  
  
  @classmethod
  def from_dict(cls, data : dict):
    """Este metodo convierte @data que se espera sea un archivo JSON-diccionario a un objeto 
        para ser almacenado en el diccionario del hilo main

    Args:
        data (_JSON_): Archivo JSON recibido como argumento para ser convertido en un objeto

    Returns:
        _Camper_: una instancia de la clase @Camper rellenada
    """
    return cls(**data)
  
  
  def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
      




# Un diccionario con datos
datos = {'a': 1, 'b': 2, 'c': 3}

# Crear una instancia de la clase Ejemplo utilizando **datos
# instancia = Ejemplo(**datos)

# Mostrar los datos de la instancia
insta = Ejemplo.from_dict(datos)

print(insta.to_JSON())