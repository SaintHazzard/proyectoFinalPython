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
    """Esta funcion recibe un objeto y lo transforma en diccionario-JSON

    Returns:
        JSON: archivo.JSON
    """
    return json.dumps(self, default=lambda o: o.__dict__, indent=4)
      

suma  = lambda x: x * 5

print((lambda x: x * 5)(2))

# Un diccionario con datos
datos = {'a': 1, 'b': 2, 'c': 3}

# Crear una instancia de la clase Ejemplo utilizando **datos
# instancia = Ejemplo(**datos)

# Mostrar los datos de la instancia
insta = Ejemplo.from_dict(datos)

print(insta.to_JSON())

def ejemplo_funcion(a, b, c):
    print(f'a={a}, b={b}, c={c}')

diccionario = {'a': 1, 'b': 2, 'c': 3}
print(*diccionario)
# ejemplo_funcion(**diccionario)