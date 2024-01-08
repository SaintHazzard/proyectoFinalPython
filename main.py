from classes.persona import * 
from classes.classAreas import *
from classes.classRutas import *

from toolsTest.visuals import *
from processJsonToMain import *
# from crearSujetos import  *



registroAspirantes = {
  
}
rutasExistentes = {
  
}
areas = {
  
}

OPCIONESAREAS = {
  "1": "Apolo",
  "2": "Artemis",
  "3": "Sputnik",
}


menu = "1. Registrar Camper\n2. Registrar prueba\n3. Nueva ruta de entrenamiento\n5. Listar personas registradas\n6. Listar rutasExistentes\n7. Listar areas de entrenamiento\n9. Crear ruta\n10. Agregar ruta a un area\n0. Salir"

if __name__=="__main__":
  
  while True:
    
    clear()
    
    print(menu)
    # for carpeta in CARPETAS:
    temporalDatosJson = from_JSOn(CARPETAS[0]);procesarJsonToCamper(Camper,registroAspirantes,temporalDatosJson)
    temporalDatosJson = from_JSOn(CARPETAS[1]);procesarJsonToCamper(areasEntrenamiento, areas,temporalDatosJson)
    temporalDatosJson = from_JSOn(CARPETAS[2]);procesarJsonToCamper(RutaEntrenamiento,rutasExistentes,temporalDatosJson)
    # procesarJsonToCamper(rutasExistentes,)
    # print(rutasExistentes)
    elec = input('Eleccion: ')
    if elec == '1':
      documentoCamper,*demasDatos=Camper.solicitar_datos_camper()
      registroAspirantes[documentoCamper] = Camper(documentoCamper,*demasDatos)
      crearJson(registroAspirantes[documentoCamper],f"{CARPETAS[0]}{documentoCamper}.json")
      wait()
    if elec == '2':
      print("***Asignar area al camper***")
      id= input('Indique el documento del camper: ')
      objetCamper = registroAspirantes[id]
      if objetCamper.verifyAreaCamper() and objetCamper.getPromedio() >= 60:
        print("\n".join([f'{key}. {value}' for key,value in OPCIONESAREAS.items()]) + "\n")
        elec = input('A que area desea agregar el camper?: ')
        
        areas[OPCIONESAREAS[elec]].agregarIntegrante(objetCamper,CARPETAS[1])
        # print(areas[OPCIONESAREAS[elec]].horarios)
      elif not objetCamper.verifyBothCal():
        print('El Camper no tiene todas las notas registradas, no se le puede asignar area')
      elif objetCamper.getPromedio() < 60:
        print(f"El camper ha reprobado la admision con nota promedio de:  {round(objetCamper.getPromedio(),2)} no se le puede asignar area")
      input('Esperar test')
      pass
    if elec == '22':
      documento=input('Documento del camper a registrar nota: ')
      if registroAspirantes[documento].getState() == 'Inscrito':
        registroAspirantes[documento].setNota()
      else: print(f"Solo puede registrar nota de campers son el estado de 'Inscrito' y el estado del camper con documento {documento} es {registroAspirantes[documento].getState()}")
      wait()
      pass
    if elec == '5':
      for documento in registroAspirantes:
        print('-'*50)
        registroAspirantes[documento].showData()
      wait()
    if elec=='6':
      for ruta in rutasExistentes:
        print('-'*50)
        rutasExistentes[ruta].printRutaEntrenamiento()
        
      wait()
      pass
    if elec=='7':
      for area in areas:
        print('-'*50)
        areas[area].printInfoArea()
        input('Esperar')
      wait()
      pass
    if elec == '9':
      nombreRuta = input('Indique nombre para la ruta de entrenamiento  ')
      ruta=RutaEntrenamiento.crearRuta(nombreRuta)
      rutasExistentes[ruta.nombres] = ruta
      print(rutasExistentes[nombreRuta].printRutaEntrenamiento())
    if elec == '10':
      AreasJson = list(from_JSOn(CARPETAS[1]).keys())
      print("Que area desea modificar? :")
      NumArea = input(("\n".join([f'{i+1}. {areas[area].nombres}' for i,area in enumerate(areas)])) + "\nEleccion: ")
      areaSeleccionada = areas[AreasJson[int(NumArea)-1]]
      areaSeleccionada.setRuta(rutasExistentes)
    if elec == '0':
      ver= input('Esta seguro que desea terminar el programa? S/N ')
      if ver == 's' or ver == 'S':
        break
      elif ver == 'n' or ver == 'N':
        continue