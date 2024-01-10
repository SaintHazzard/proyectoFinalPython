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
    
def submenutrainer(TRAINERS,RUTAS,DATA):
  OPCIONES = {
        "1" : "Listar Trainers",
    # "2" : "Crear rutas",
    "2" : "Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.",
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
  pass