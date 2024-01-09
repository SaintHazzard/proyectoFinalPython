
from toolsTest.visuals import *
from classes.classRutas import *
def submenucamper(data):
  OPCIONES = {
    "1" : "Ingreso de notas",
    '2' : "Listar Campers",
    "3" : "Listar Campers con bajo rendimiento",
    "0" : "Menu anterior"
  }

  elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
  if elec in OPCIONES:
    if elec == "1":
      documento=input('Documento del camper a registrar nota: ')
      if data[documento].getState() == 'Inscrito':
        data[documento].setNota()
      else: print(f"Solo puede registrar nota de campers son el estado de 'Inscrito' y el estado del camper con documento {documento} es {data[documento].getState()}")
      wait()
      
    elif elec is "2":
      for documento in data:
        print('-'*50)
        data[documento].showData()
      wait()
      pass
    
    
    

        
        
        

  else: print("Eleccion no valida, Ingrese una opcion valida")
  pass
