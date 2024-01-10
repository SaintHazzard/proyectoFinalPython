import os
import time

def sleep():
    time.sleep(1)

def clear():
    # os.system('cls')
    os.system('clear')
def wait():
     input("Presiona Enter para continuar...")
     
if __name__ == "__main__":
  pass
   

def mostrar_error(mensaje):
    print(f"{'*' * 5} Error: {mensaje} No válido {'*' * 5}")
    


def separacion():
  print("\t"+"*" * 50)
  wait()