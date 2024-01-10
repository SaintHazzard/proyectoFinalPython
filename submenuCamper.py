
from toolsTest.visuals import *
from classes.classRutas import *
def submenucamper(data):
  OPCIONES = {
    "1" : "Ingreso de notas",
    '2' : "Listar inscritos",
    "3" : "Listar Campers con bajo rendimiento",
    "4" : "Listar Campers aprobados",
    # "5" : "Agregar notas de modulos",
    "0" : "Menu anterior"
  }
  while True:
    clear()
    elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
    if elec in OPCIONES:
      if elec == "1":
        print()
        for i in data:
          if data[i].estado:
            print(f'Documento: {data[i].documento} {data[i].nombres} {data[i].apellidos}')
        documento=input('Documento del camper a registrar nota: ')
        
        estado = data[documento].getState()
        if estado == 'Inscrito' or "Aprobado":
          data[documento].setNota()
        else: print(f"Solo puede registrar nota de campers con el estado de 'Inscrito' y el estado del camper con documento {documento} es {data[documento].getState()}")
        separacion()
        
      elif elec is "2":
        for documento in data:
          print('-'*50)
          data[documento].showData()
        separacion()
        pass
      elif elec is "3":
        print('Los campers con bajo rendimiento son: ')
        for documento in data:
          camper = data[documento]
          if camper.riesgo == 'Alto':
            ultimaLlave = list(camper.notasHistory.keys())[-1]
            print(ultimaLlave)
            print(f'Nombre: {camper.nombres} esta en riesgo {camper.riesgo} su nota en el ultimo modulo {ultimaLlave} fue {camper.notasHistory[ultimaLlave]["nota final"]}')
        separacion()
        pass
      elif elec is "4":
        print(f'Los campers aprobados fueron: ')
        for documento in data:
          data[documento].showDataAprobado()
        separacion()
        pass
      elif elec is "0":
        break
      
      
      

          
          
          

    else: 
      print("Eleccion no valida, Ingrese una opcion valida")
      separacion()
    pass
