import traceback
import sys

def funcion_que_lanza_un_error():
    raise ValueError("Input invalido")

try:
    funcion_que_lanza_un_error()
except Exception as e:
    print(sys.exc_info())
    exc_type, exc_value, exc_traceback = sys.exc_info()

    if exc_traceback:
        tb_info = traceback.extract_tb(exc_traceback)
        # print(tb_info)
        line = tb_info[-1][1]
        print(line)
        # print(f"Error en la línea {line}: {exc_type.__name__}: {exc_value}")
    else:
        print(f"Error: {exc_type.__name__}: {exc_value}")