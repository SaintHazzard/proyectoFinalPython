from toolsTest.visuals import *
def listarCamperTrainer(RUTAS,DATA,TRAINERS):
  print("Que ruta desea consultar: ")
  elec = input("\n".join([f'{key+1}. {value}' for key,value in enumerate(RUTAS.keys())]) + "\nEleccion: ")
  RUTASNAME = list(RUTAS.keys())
  for trainer in TRAINERS:
    if RUTASNAME[int(elec)-1] in TRAINERS[trainer].rutas:
      print(f'El Trainer {TRAINERS[trainer].nombres} esta vinculado a la ruta {RUTASNAME[int(elec)-1]}')
  wait()
  for camper in DATA:
    if DATA[camper].ruta:
      if RUTASNAME[int(elec)-1] == DATA[camper].ruta['nombres']:
        print(f'El Camper {DATA[camper].nombres} esta vinculado a la ruta {RUTASNAME[int(elec)-1]}')
def listarCamperModulo(RUTAS,DATA,TRAINERS):
  print("Que ruta desea consultar: ")
  elec = input("\n".join([f'{key+1}. {value}' for key,value in enumerate(RUTAS.keys())]) + "\nEleccion: ")
  if not elec.isdigit():
    print('Eleccion no valida')
    wait()
    return
  print("Que trainer desea consultar: ")
  elecTrainer = input("\n".join([f'{key+1}. {value.nombres}' for key,value in enumerate(TRAINERS.values())]) + "\nEleccion: ")
  RUTASNAME = list(RUTAS.keys())
  TRAINERSNAME = list(TRAINERS.keys())
  if len(TRAINERSNAME) > 0:
    if RUTASNAME[int(elec)-1] in TRAINERS[TRAINERSNAME[int(elecTrainer)-1]].rutas:
      print(f'El trainer {TRAINERS[TRAINERSNAME[int(elecTrainer)-1]].nombres} con la ruta {RUTASNAME[int(elec)-1]}')
      print(f'Los camper aprobados en el ultimo modulo con el Trainer {TRAINERS[TRAINERSNAME[int(elecTrainer)-1]].nombres} fueron: ')
      for camper in DATA:
        if DATA[camper].ruta:
          if RUTASNAME[int(elec)-1] in DATA[camper].ruta['nombres'] and DATA[camper].riesgo == 'Bajo':
            DATA[camper].showData()
      wait()     
      print(f'Los camper reprobados en el ultimo modulo con el Trainer {TRAINERS[TRAINERSNAME[int(elecTrainer)-1]].nombres} fueron: ')
      for camper in DATA:
        if DATA[camper].ruta:
          if RUTASNAME[int(elec)-1] in DATA[camper].ruta['nombres'] and DATA[camper].riesgo == 'Alto':
            DATA[camper].showData()
    wait()     
    pass
  else: print('El trainer no tiene asignado esa ruta.');wait()
  pass
    
def submenutrainer(TRAINERS,RUTAS,DATA):
  OPCIONES = {
        "1" : "Listar Trainers",
    # "2" : "Crear rutas",
    "2" : "Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.",
    "3" : 'Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado',
    # "3" : "Asignar ruta a area de entrenamiento",
    # "4" : "Listar Rutas existentes",
    # "5" : "Listar Areas de entrenamiento",
    
    
    "0" : "Menu principal"
  }
  elec = input("\n".join([f'{key}. {value}' for key,value in OPCIONES.items()]) + "\nEleccion: ")
  if elec is "1":
    for trainer in TRAINERS:
      TRAINERS[trainer].showTrainer()
    wait()
  elif elec is '2':
    listarCamperTrainer(RUTAS,DATA,TRAINERS)
    wait()
    pass
  elif elec is "3":
    listarCamperModulo(RUTAS,DATA,TRAINERS)
    pass