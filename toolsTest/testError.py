import traceback
import sys

def raiseError():
    raise ValueError

try:
    raiseError()
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()

    if exc_traceback:
        tb_info = traceback.extract_tb(exc_traceback)
        # print(tb_info)
        line = tb_info[-1][1]
        print(f"Error en la línea {line}: {exc_type.__name__}: {exc_value}")
    else:
        print(f"Error: {exc_type.__name__}: {exc_value}")