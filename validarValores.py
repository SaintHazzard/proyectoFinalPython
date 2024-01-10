def value0To100(value):
    try:
        if not (0 <= value <= 100):
            raise ValueError(f'El valor {value} está fuera del rango 0 - 100, ingrese un valor en el rango')
        print('Nota registrada')
        return True
    except ValueError as e:
        print(e)
        return False
  
def mostrar_error(mensaje):
    print(f"{'*' * 5} Error: {mensaje} No válido {'*' * 5}")