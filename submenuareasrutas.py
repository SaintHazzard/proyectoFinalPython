from classes.classRutas import *
from toolsTest.visuals import *
from processJsonToMain import *
def submenuareasyrutas(DATA,AREAS,RUTAS,TRAINERS,CARPETAS):
  OPCIONES = {
        "1" : "Asignar area al camper",
    "2" : "Crear rutas",
    "3" : "Asignar trainer, ruta, area y horario",
    # "3" : "Asignar ruta a area de entrenamiento",
    "4" : "Listar Rutas existentes",
    "5" : "Listar Areas de entrenamiento",
    
    "0" : "Menu principal"
  }
  OPCIONESAREAS = {
  "1": "Apolo",
  "2": "Artemis",
  "3": "Sputnik",
} 
  while True:
    clear()
    elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
    if elec is "1":
      print("***Asignar area al camper***")
      id= input('Indique el documento del camper: ')
      objetCamper = DATA[id]
      if objetCamper.verifyAreaCamper() and objetCamper.getPromedio() >= 60 and len(objetCamper.notas) == 2:
        print("\n".join([f'{key}. {value}' for key,value in OPCIONESAREAS.items()]) + "\n")
        elec = input('A que area desea agregar el camper?: ')
        AREAS[OPCIONESAREAS[elec]].agregarIntegrante(objetCamper,CARPETAS[1],RUTAS)
        # print(areas[OPCIONESAREAS[elec]].horarios)
        objetCamper.verifyBothCal()
      elif objetCamper.getPromedio() < 60 and len(objetCamper.notas) == 2 and (objetCamper.notas['nota teorica'] and objetCamper.notas['nota practica']):
        print(f"El camper ha reprobado la admision con nota promedio de:  {round(objetCamper.getPromedio(),2)} no se le puede asignar area")
      elif objetCamper.estado == 'Inscrito':
        print(f'El camper esta en esta inscrito {objetCamper.notas} registrar las notas faltantes')
      elif objetCamper.estado == 'Aprobado':
        print('El camper ya esta asignado a un area')
    elif elec is "2":
        nombreRuta = input('Indique nombre para la ruta de entrenamiento  ')
        ruta=RutaEntrenamiento.crearRuta(nombreRuta)
        RUTAS[ruta.nombres] = ruta
        # print(rutasExistentes[nombreRuta].printRutaEntrenamiento())
        pass
    # elif elec is "3":
      
    #   temporalDatosJson = from_JSOn(CARPETAS[2]);procesarJsonToCamper(RutaEntrenamiento,RUTAS,temporalDatosJson)
    #   AreasJson = list(from_JSOn(CARPETAS[1]).keys())
    #   print("Que area desea modificar? ")
    #   NumArea = input(("\n".join([f'{i+1}. {AREAS[area].nombres}' for i,area in enumerate(AREAS)])) + "\nEleccion: ")
    #   areaSeleccionada = AREAS[AreasJson[int(NumArea)-1]]
    #   areaSeleccionada.setRuta(RUTAS,DATA)
    elif elec is "4":
      for ruta in RUTAS:
        print('-'*50)
        RUTAS[ruta].printRutaEntrenamiento()
    elif elec is "5":
      for area in AREAS:
        print('-'*50) 
        AREAS[area].printInfoArea()
        pass
    elif elec is "3":
      documento=input('Numero de documento del trainer: ')
      TRAINERS[documento].setTrainerRutaArea(RUTAS,AREAS)
    
    elif elec is "0":
      break
    else : 
      print("Eleccion no valida, Ingrese una opcion valida")
    wait()