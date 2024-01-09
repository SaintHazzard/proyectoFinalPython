from classes.classRutas import *
from toolsTest.visuals import *
def submenuareasyrutas(data,areas,rutasExistentes,CARPETAS):
  OPCIONES = {
        "1" : "Asignar area al camper",
    "2" : "Crear rutas",
    "3" : "Asignar ruta a area de entrenamiento",
    "4" : "Rutas existentes",
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
      objetCamper = data[id]
      if objetCamper.verifyAreaCamper() and objetCamper.getPromedio() >= 60:
        print("\n".join([f'{key}. {value}' for key,value in OPCIONESAREAS.items()]) + "\n")
        elec = input('A que area desea agregar el camper?: ')
        areas[OPCIONESAREAS[elec]].agregarIntegrante(objetCamper,CARPETAS[1])
        # print(areas[OPCIONESAREAS[elec]].horarios)
        objetCamper.verifyBothCal()
      elif objetCamper.getPromedio() < 60 and len(objetCamper.notas) == 2:
        print(f"El camper ha reprobado la admision con nota promedio de:  {round(objetCamper.getPromedio(),2)} no se le puede asignar area")
    if elec is "2":
        nombreRuta = input('Indique nombre para la ruta de entrenamiento  ')
        ruta=RutaEntrenamiento.crearRuta(nombreRuta)
        rutasExistentes[ruta.nombres] = ruta
        # print(rutasExistentes[nombreRuta].printRutaEntrenamiento())
        pass
    elif elec is "3":
      AreasJson = list(from_JSOn(CARPETAS[1]).keys())
      print("Que area desea modificar? ")
      NumArea = input(("\n".join([f'{i+1}. {areas[area].nombres}' for i,area in enumerate(areas)])) + "\nEleccion: ")
      areaSeleccionada = areas[AreasJson[int(NumArea)-1]]
      areaSeleccionada.setRuta(rutasExistentes,data)
    elif elec is "4":
      for ruta in rutasExistentes:
        print('-'*50)
        rutasExistentes[ruta].printRutaEntrenamiento()
    elif elec is "5":
      for area in areas:
        print('-'*50) 
        areas[area].printInfoArea()
        pass
    
    elif elec is "0":
      break
    wait()